# -*- coding: utf-8 -*-
import inspect
import abc
from typing import List, Any, Optional, Type, Dict

from a3py.improved.json import fast_loads
from django.core.exceptions import ValidationError
from django.http import FileResponse
from django.db.models import JSONField
from django.views.generic import View

from a3dj.core import inner_errors
from a3dj.core.response_utils import build_success_response, FileResponseStruct
from a3dj.structs import json_structs
from a3dj.structs.form_structs.base_form_struct import BaseFormStruct
from a3dj.structs.json_structs.base_json_struct import BaseJsonStruct
from a3dj.structs.mockers import FixedValueMocker
from a3dj.errors import CRequestStructError
from a3dj.structs.fields import ListField, ModelMultipleInstanceField

from .base_request_permission import BaseRequestPermission


class DynamicResponseStruct(json_structs.JsonStruct):

    class Meta(json_structs.JsonStructOptions):
        is_abstract = True


class BasePostViewMetaClass(abc.ABCMeta):

    def __new__(mcs, name, bases, attrs: dict, **kwargs):
        # exclude self
        parents = [b for b in bases if isinstance(b, BasePostViewMetaClass)]
        if not parents:
            return super().__new__(mcs, name, bases, attrs, **kwargs)

        # new class
        new_cls = super().__new__(mcs, name, bases, attrs, **kwargs)

        if inspect.isabstract(new_cls):
            # 复杂动态组装情况
            return new_cls

        r = new_cls.handle_business.__annotations__.get('return', None) # noqa
        if r == DynamicResponseStruct and getattr(new_cls, 'data_response_struct_cls', None) is None:
            # 直接让data_response_struct_cls成为DynamicResponseStruct的情况
            return new_cls

        if inspect.isclass(r) and issubclass(r, FileResponse):
            new_cls.response_struct_cls = FileResponseStruct
            new_cls.data_response_struct_cls = None
            return new_cls

        # dynamic build response struct
        class SuccessResponseStruct(json_structs.JsonStruct):
            status = json_structs.CharField(mocker=FixedValueMocker('OK'), default='OK')

        response_struct_cls = SuccessResponseStruct
        data_response_struct_cls = None

        def _check_data_response_struct_cls(data_cls: Type[json_structs.JsonStruct]):
            if len(data_cls.get_meta().fields) == 0:
                raise inner_errors.ViewError(f"Invalid view {new_cls.__name__} response data struct: empty fields.")

        if r is None:
            pass
        elif issubclass(r, DynamicResponseStruct):
            data_response_struct_cls = new_cls.dynamic_build_response_struct() # noqa
            _check_data_response_struct_cls(data_response_struct_cls)
            response_struct_cls.dynamic_add_field('data', json_structs.ObjectField(obj_cls=data_response_struct_cls))

        elif issubclass(r, (json_structs.JsonStruct, json_structs.ModelJsonStruct)):
            data_response_struct_cls = r
            _check_data_response_struct_cls(data_response_struct_cls)
            response_struct_cls.dynamic_add_field('data', json_structs.ObjectField(obj_cls=data_response_struct_cls))

        else:
            raise inner_errors.ViewError(f"Invalid view {new_cls.__name__} response struct type: {r.__name__}")

        new_cls.response_struct_cls = response_struct_cls
        new_cls.data_response_struct_cls = data_response_struct_cls
        return new_cls


class BasePostView(View, metaclass=BasePostViewMetaClass):
    response_struct_cls: json_structs.JsonStruct
    data_response_struct_cls: json_structs.JsonStruct

    request_permissions: List[BaseRequestPermission] = None
    request_struct_cls = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._request_data: Optional[Dict] = None

    @abc.abstractmethod
    def handle_business(self, request_struct, custom_params):
        raise NotImplementedError()

    def post(self, *_, **__):
        for permission in self.request_permissions or list():
            permission(self.request)

        request_struct = self.validate_request_struct()
        custom_params = self.custom_validate(request_struct)

        r = self.handle_business(request_struct, custom_params)

        if r is None:
            return build_success_response()
        elif isinstance(r, BaseJsonStruct):
            return build_success_response(data=r.to_json_dict())
        elif isinstance(r, FileResponse):
            return r
        else:
            raise inner_errors.ViewError(f"Invalid response type: {type(r).__name__}")

    def custom_validate(self, request_struct) -> Any:
        pass

    def _get_json_request_data(self) -> dict:
        try:
            return fast_loads(self.request.body)
        except Exception as __:
            raise CRequestStructError(JSONField.default_error_messages['invalid'])

    def _get_form_request_data(self):
        return self.request.POST

    def _get_form_request_files(self):
        return self.request.FILES

    def _get_request_data(self) -> dict:
        if self._request_data is not None:
            return self._request_data

        d = dict()
        if self.request_struct_cls is not None and inspect.isclass(self.request_struct_cls):
            if issubclass(self.request_struct_cls, BaseJsonStruct):
                d.update(self._get_json_request_data() or dict())
            elif issubclass(self.request_struct_cls, BaseFormStruct):
                d.update(self._get_form_request_data() or dict())
                d.update(self._get_form_request_files() or dict())

                for field_name, field_instance in self.request_struct_cls.get_meta().fields.items():
                    vl = d.get(field_name, None)
                    if vl is None:
                        continue

                    if isinstance(field_instance, (ListField, ModelMultipleInstanceField)):
                        d[field_name] = vl
                    else:
                        d[field_name] = vl[0]

            else:
                raise inner_errors.ViewError(f"Invalid request struct type: {self.request_struct_cls.__name__}")

        self._request_data = d
        return self._request_data

    @classmethod
    def _full_clean_request_struct(cls, request_struct):
        try:
            request_struct.full_clean()
        except ValidationError as e:
            raise CRequestStructError(str(e), repr(e))

    def validate_request_struct(self) -> Optional[json_structs.JsonStruct]:
        request_struct = None

        if self.request_struct_cls is not None and inspect.isclass(self.request_struct_cls):
            data = self._get_request_data()
            request_struct = self.request_struct_cls(data)
            self._full_clean_request_struct(request_struct)

        return request_struct

    @classmethod
    def dynamic_build_response_struct(cls) -> Type[json_structs.JsonStruct]:
        pass
