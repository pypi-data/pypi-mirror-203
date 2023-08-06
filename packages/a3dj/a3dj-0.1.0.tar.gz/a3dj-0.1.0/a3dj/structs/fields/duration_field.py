# -*- coding: utf-8 -*-
import datetime
from django.core.exceptions import ValidationError
from django.db.models.fields import DurationField as DjangoDurationField
from django.utils.dateparse import parse_duration

from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import DurationMocker, BaseMocker


class DurationFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'duration'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class DurationFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return DurationMocker()


class DurationField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: DjangoDurationField) -> 'DurationField':
        return cls()

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return DurationFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return DurationFieldMockManager(self)

    def to_python(self, value) -> datetime.timedelta:
        if isinstance(value, datetime.timedelta):
            return value

        try:
            parsed = parse_duration(value)
        except ValueError:
            pass
        else:
            if parsed is not None:
                return parsed

        raise ValidationError(
            DjangoDurationField.default_error_messages["invalid"],
            code="invalid",
            params={"value": value},
        )

    def to_json(self, value: datetime.timedelta) -> str:
        return str(value)
