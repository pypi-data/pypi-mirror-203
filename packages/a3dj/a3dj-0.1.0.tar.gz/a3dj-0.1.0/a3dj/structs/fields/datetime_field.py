# -*- coding: utf-8 -*-
import datetime
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models.fields import DateTimeField as DjangoDateTimeField

from a3py.simplified.datetime import datetime2str
from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import DateTimeMocker, BaseMocker


class DateTimeFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'datetime'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class DateTimeFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return DateTimeMocker()


class DateTimeField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: DjangoDateTimeField) -> 'DateTimeField':
        return cls()

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return DateTimeFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return DateTimeFieldMockManager(self)

    def to_python(self, value) -> datetime.datetime:
        if isinstance(value, datetime.datetime):
            parsed = value
        else:
            try:
                parsed = datetime.datetime.fromisoformat(str(value))
            except ValueError:
                raise ValidationError(
                    DjangoDateTimeField.default_error_messages["invalid_datetime"],
                    code="invalid_datetime",
                    params={"value": value},
                )

        if settings.USE_TZ and not timezone.is_aware(parsed):
            parsed = timezone.make_aware(parsed)
        return parsed

    def to_json(self, value: datetime.datetime) -> str:
        return datetime2str(value)
