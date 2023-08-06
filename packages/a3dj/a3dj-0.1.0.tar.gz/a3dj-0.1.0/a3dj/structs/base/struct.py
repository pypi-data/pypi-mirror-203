# -*- coding: utf-8 -*-
import copy
import abc
from typing import Dict, Type, Set, Optional
from django.core.exceptions import ValidationError

from a3dj.patches import PatchedValidationError
from a3dj.structs.base.base_field import BaseField


class StructOptions:
    fields: Dict[str, BaseField]

    verbose_name = None
    description = None
    is_component = False
    is_abstract = False


class StructMetaClass(abc.ABCMeta):

    @abc.abstractmethod
    def _check_field(cls, field_name: str, field_instance: BaseField):
        raise NotImplementedError()

    def _get_meta(cls, meta: Optional[Type[StructOptions]]) -> StructOptions:
        if meta is None:
            return StructOptions()
        else:
            return meta()

    def _check_meta(cls):
        pass

    def _add_other_fields(cls, field_name_set: Set[str]):
        pass

    def __new__(mcs, name, bases, attrs: dict, **kwargs):
        # exclude self
        parents = [b for b in bases if isinstance(b, StructMetaClass)]
        if not parents:
            return super().__new__(mcs, name, bases, attrs, **kwargs)

        # 用于继承时，排除父类的字段
        field_name_set = set()
        # new fields
        fields = dict()
        for field_name, field_instance in attrs.items():
            field_name_set.add(field_name)

            if isinstance(field_instance, BaseField):
                if field_instance.verbose_name is None:
                    field_instance.verbose_name = field_name.replace("_", " ")

                fields[field_name] = field_instance

        for field_name in fields.keys():
            attrs.pop(field_name)

        # new class
        meta = attrs.pop("Meta", None)
        new_cls = super().__new__(mcs, name, bases, attrs, **kwargs)

        # check fields
        for field_name, field_instance in fields.items():
            new_cls._check_field(field_name, field_instance)

        # set meta
        meta = new_cls._get_meta(meta)
        meta.fields = fields
        new_cls._meta = meta

        # abstract struct ends here
        if meta.is_abstract:
            return new_cls

        # check meta
        new_cls._check_meta()

        # parent fields
        mro_structs = new_cls.mro()
        if len(mro_structs) > 3:
            parent_structs = mro_structs[1: -2]

            for parent in parent_structs:
                if not hasattr(parent, '_meta'):
                    break

                parent: Type['Struct']
                parent_fields = parent.get_meta().fields

                for name, field in parent_fields.items():
                    new_field = copy.deepcopy(field)
                    if name not in field_name_set:
                        fields[name] = new_field
                        field_name_set.add(name)

        # other fields
        new_cls._add_other_fields(field_name_set)

        # bind to class
        for field_name, field_instance in fields.items():
            field_instance.contribute_to_struct(new_cls, field_name)

        return new_cls


class Struct:
    _meta: StructOptions

    @classmethod
    def get_meta(cls):
        return cls._meta

    def __init__(self, data=None, **kwargs):
        field_list = list()
        for field_name, field_instance in self.get_meta().fields.items():
            field_list.append(field_name)
            setattr(self, field_name, None)

        if data is not None:
            is_dict = isinstance(data, dict)
            for k in field_list:
                if is_dict:
                    v = data.get(k, None)
                else:
                    v = getattr(data, k, None)

                if v is not None:
                    setattr(self, k, v)

        for k, v in kwargs.items():
            if k in field_list:
                setattr(self, k, v)

    @classmethod
    def dynamic_add_field(cls, name: str, instance: BaseField):
        cls._meta.fields[name] = instance

    def clean(self):
        # 推荐只抛出ValidationError
        pass

    def _clean_fields(self):
        for field_name, field_instance in self._meta.fields.items():
            value = getattr(self, field_name, None)

            try:
                value = field_instance.clean_for_python(value, self)
            except ValidationError as e:
                e: PatchedValidationError

                e.set_field(field_name)
                raise e

            setattr(self, field_name, value)

    def full_clean(self):
        self._clean_fields()
        self.clean()

    # 仅输出时用，所以不用clean_for_python，如有需要可手动full_clean
    def to_json_dict(self) -> dict:
        rd = dict()
        for field_name, field_instance in self._meta.fields.items():
            value = getattr(self, field_name, None)
            try:
                value = field_instance.clean_for_json(value, self)
            except ValidationError as e:
                e: PatchedValidationError

                e.set_field(field_name)
                raise e

            rd[field_name] = value

        return rd

    def __repr__(self):
        return f"<{self.__class__.__name__}: object>"

    def __str__(self):
        return f"{self.__class__.__name__}"

    @classmethod
    @abc.abstractmethod
    def to_application_open_api_dict(cls) -> dict:
        raise NotImplementedError()

    @classmethod
    def mock(cls, instance=None, root_instance=None): # noqa
        this_instance = cls()
        if root_instance is None:
            root_instance = this_instance

        for field_name, field_instance in cls._meta.fields.items():
            mock_value = field_instance.mock_manager.mock(instance=this_instance, root_instance=root_instance)
            setattr(this_instance, field_name, mock_value)

        return this_instance
