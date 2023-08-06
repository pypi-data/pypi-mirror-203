# -*- coding: utf-8 -*-
import uuid

from django.core.exceptions import ValidationError
from django.db.models.fields import UUIDField as DjangoUUIDField

from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import UUIDMocker, BaseMocker


class UUIDFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'uuid'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class UUIDFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return UUIDMocker()


class UUIDField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: DjangoUUIDField) -> 'UUIDField':
        return cls()

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return UUIDFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return UUIDFieldMockManager(self)

    def to_python(self, value) -> uuid.UUID:
        if isinstance(value, uuid.UUID):
            return value

        try:
            return uuid.UUID(value)
        except (AttributeError, ValueError):
            raise ValidationError(
                DjangoUUIDField.default_error_messages["invalid"],
                code="invalid",
                params={"value": value},
            )

    def to_json(self, value: uuid.UUID) -> str:
        return str(value)
