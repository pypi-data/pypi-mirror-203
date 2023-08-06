# -*- coding: utf-8 -*-
from typing import Type, TYPE_CHECKING

from django.core.exceptions import ValidationError
from django.db.models import Field as ModelField
from django.utils.translation import gettext_lazy as _

from a3dj.core.inner_errors import ModelFieldTranslateError, MixingError
from a3dj.structs.base.base_field import BaseField, JsonType, BaseFieldMockManager, BaseFieldOpenApiManager
from a3dj.structs.mockers import ObjectMocker, BaseMocker

if TYPE_CHECKING:
    from a3dj.structs.json_structs.base_json_struct import BaseJsonStruct


class ObjectFieldOpenApiManager(BaseFieldOpenApiManager):
    field: 'ObjectField'

    @classmethod
    def _preset_form_type(cls) -> str:
        raise MixingError("FormStruct cannot use ObjectField")

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'object'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.Object

    def _build_json_base_info(self) -> dict:
        info = super()._build_json_base_info()
        obj_info = self.field.obj_cls.to_json_open_api_dict()
        info.update(obj_info)
        return info

    def get_components(self) -> dict:
        components = dict()
        sub_components = self.field.obj_cls.get_open_api_components()
        if isinstance(sub_components, dict) and len(sub_components) > 0:
            components.update(sub_components)

        return components


class ObjectFieldMockManager(BaseFieldMockManager):
    field: 'ObjectField'

    def _preset_default_mocker(self) -> BaseMocker:
        return ObjectMocker(obj_cls=self.field.obj_cls)


class ObjectField(BaseField):

    default_error_messages = {
        "invalid_type": _("This field's type must be a correct object or a dict, not “%(value)s”."),
    }

    @classmethod
    def _build_from_model_field(cls, field_instance: ModelField) -> 'BaseField':
        raise ModelFieldTranslateError("No field can translate to ObjectField")

    @classmethod
    def support_form(cls) -> bool:
        return False

    @classmethod
    def support_json(cls) -> bool:
        return True

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return ObjectFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return ObjectFieldMockManager(self)

    def __init__(self, obj_cls: Type['BaseJsonStruct'], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.obj_cls = obj_cls

    def to_python(self, value) -> 'BaseJsonStruct':
        if isinstance(value, dict):
            obj_instance = self.obj_cls(**value)
        elif isinstance(value, self.obj_cls):
            obj_instance = value
        else:
            raise ValidationError(
                message=self.default_error_messages["invalid_type"],
                code="invalid_type",
                params={"value": type(value)}
            )

        obj_instance.full_clean()
        return obj_instance

    def to_json(self, value: 'BaseJsonStruct') -> dict:
        return value.to_json_dict()
