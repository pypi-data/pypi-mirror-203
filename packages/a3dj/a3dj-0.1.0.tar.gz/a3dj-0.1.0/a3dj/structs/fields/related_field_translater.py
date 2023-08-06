# -*- coding: utf-8 -*-
from typing import Dict, Type
from django.db import models

from a3dj.structs.base.base_field import BaseField
from a3dj.structs import fields
from a3dj.core.inner_errors import ModelFieldTranslateError


class RelatedFieldTranslater:
    cached_mappings = dict()
    mappings: Dict[Type[models.Field], Type[BaseField]] = {
        models.IntegerField: fields.IntegerField,
        models.CharField: fields.CharField,
        models.BooleanField: fields.BooleanField
    }

    @classmethod
    def translate(cls, field_instance: models.Field) -> BaseField:
        json_field_cls = cls._get_struct_field_cls(type(field_instance))
        return json_field_cls.build_from_model_field(field_instance)

    @classmethod
    def _get_struct_field_cls(cls, field_cls) -> Type[BaseField]:
        cls_name = field_cls.__name__

        cache_result = cls.cached_mappings.get(cls_name, None)
        if cache_result is not None:
            return cache_result

        for f_cls in field_cls.__mro__:
            json_field_cls = cls.mappings.get(f_cls, None)
            if json_field_cls is not None:
                cls.cached_mappings[cls_name] = json_field_cls
                return json_field_cls

        raise ModelFieldTranslateError(f"{cls_name} can not find corresponding field class.")
