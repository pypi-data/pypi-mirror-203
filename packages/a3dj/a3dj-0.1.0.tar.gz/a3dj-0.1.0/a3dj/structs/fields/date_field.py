# -*- coding: utf-8 -*-
import datetime

from django.core.exceptions import ValidationError
from django.db.models.fields import DateField as DjangoDateField

from a3py.simplified.datetime import date2str
from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import DateMocker, BaseMocker


class DateFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'date'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class DateFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return DateMocker()


class DateField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: DjangoDateField) -> 'DateField':
        return cls()

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return DateFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return DateFieldMockManager(self)

    def to_python(self, value) -> datetime.date:
        if isinstance(value, datetime.date):
            return value

        try:
            return datetime.date.fromisoformat(str(value))
        except ValueError:
            raise ValidationError(
                DjangoDateField.default_error_messages["invalid_date"],
                code="invalid_date",
                params={"value": value},
            )

    def to_json(self, value: datetime.date) -> str:
        return date2str(value)
