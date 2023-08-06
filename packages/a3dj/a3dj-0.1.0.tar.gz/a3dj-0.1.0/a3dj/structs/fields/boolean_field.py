# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db.models import Field as ModelField
from django.db.models.fields import BooleanField as DjangoBooleanField

from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import BooleanMocker, BaseMocker


class BooleanFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'boolean'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.Boolean


class BooleanFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return BooleanMocker()


class BooleanField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: ModelField) -> 'BooleanField':
        return cls()

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return BooleanFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return BooleanFieldMockManager(self)

    def to_python(self, value) -> bool:
        if isinstance(value, bool):
            return value

        value = str(value).lower()

        if value in ('t', 'true', '1'):
            return True

        if value in ('f', 'false', '0'):
            return False

        raise ValidationError(
            message=DjangoBooleanField.default_error_messages["invalid"],
            code="invalid",
            params={"value": value},
        )

    def to_json(self, value: bool) -> bool:
        return value
