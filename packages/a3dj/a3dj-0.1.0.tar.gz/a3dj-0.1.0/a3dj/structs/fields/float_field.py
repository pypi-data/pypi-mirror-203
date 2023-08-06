# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db.models import FloatField as ModelFloatField

from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import FloatMocker, BaseMocker


class FloatFieldOpenApiManager(BaseFieldOpenApiManager):
    field: 'FloatField'

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.Number

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'float'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.Number


class FloatFieldMockManager(BaseFieldMockManager):
    field: 'FloatField'

    def _preset_default_mocker(self) -> BaseMocker:
        return FloatMocker()


class FloatField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: ModelFloatField) -> 'FloatField':
        return cls()

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return FloatFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return FloatFieldMockManager(self)

    def to_python(self, value) -> float:
        if isinstance(value, float):
            return value

        try:
            return float(str(value))
        except (TypeError, ValueError):
            raise ValidationError(
                message=ModelFloatField.default_error_messages["invalid"],
                code="invalid",
                params={"value": value},
            )

    def to_json(self, value: float) -> float:
        return value
