# -*- coding: utf-8 -*-
from a3dj.structs.base.base_field import BaseFieldOpenApiManager
from .integer_field import IntegerField, IntegerFieldOpenApiManager


class PositiveIntegerFieldOpenApiManager(IntegerFieldOpenApiManager):
    field: 'PositiveIntegerField'

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'positive'


class PositiveIntegerField(IntegerField):

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return PositiveIntegerFieldOpenApiManager(self)

    def __init__(self, min_value: int = None, *args, **kwargs):
        if min_value is None or min_value < 1:
            min_value = 1
        super().__init__(min_value=min_value, *args, **kwargs)
