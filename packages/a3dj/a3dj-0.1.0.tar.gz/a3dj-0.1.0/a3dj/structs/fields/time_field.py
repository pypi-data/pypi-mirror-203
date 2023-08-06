# -*- coding: utf-8 -*-
import datetime
from django.core.exceptions import ValidationError
from django.db.models.fields import TimeField as DjangoTimeField

from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import TimeMocker, BaseMocker


class TimeFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'time'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class TimeFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return TimeMocker()


class TimeField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: DjangoTimeField) -> 'TimeField':
        return cls()

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return TimeFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return TimeFieldMockManager(self)

    def to_python(self, value) -> datetime.time:
        if isinstance(value, datetime.time):
            return value

        try:
            return datetime.time.fromisoformat(str(value)).replace(tzinfo=None)
        except ValueError:
            raise ValidationError(
                DjangoTimeField.default_error_messages["invalid_time"],
                code="invalid_time",
                params={"value": value},
            )

    def to_json(self, value: datetime.time) -> str:
        return str(value)
