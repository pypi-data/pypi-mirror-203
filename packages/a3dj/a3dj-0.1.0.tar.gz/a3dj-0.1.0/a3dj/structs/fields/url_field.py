# -*- coding: utf-8 -*-
from django.core import validators

from a3dj.structs.base.base_field import BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import URLMocker, BaseMocker

from .char_field import CharField


class URLFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'url'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class URLFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return URLMocker()


class URLField(CharField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(validators.URLValidator())

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return URLFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return URLFieldMockManager(self)
