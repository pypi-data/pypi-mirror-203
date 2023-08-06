# -*- coding: utf-8 -*-
from decimal import Decimal, DecimalException

from django.core.exceptions import ValidationError
from django.db.models.fields import DecimalField as DjangoDecimalField

from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import DecimalMocker, BaseMocker


class DecimalFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'decimal'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class DecimalFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return DecimalMocker()


class DecimalField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: DjangoDecimalField) -> 'DecimalField':
        return cls()

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return DecimalFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return DecimalFieldMockManager(self)

    def to_python(self, value) -> Decimal:
        if isinstance(value, Decimal):
            return value

        try:
            return Decimal(str(value))
        except DecimalException:
            raise ValidationError(
                DjangoDecimalField.default_error_messages["invalid"],
                code="invalid",
                params={"value": value},
            )

    def to_json(self, value: Decimal) -> str:
        return str(value)
