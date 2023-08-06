# -*- coding: utf-8 -*-
import json
from typing import Any, Tuple

from django.core.exceptions import ValidationError
from django.db.models import JSONField as ModelJSONField

from a3dj.structs.base.base_field import BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import NoneMocker, BaseMocker

from .char_field import CharField


class JSONFieldOpenApiManager(BaseFieldOpenApiManager):

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'json'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class JSONFieldMockManager(BaseFieldMockManager):

    def _preset_default_mocker(self) -> BaseMocker:
        return NoneMocker()


class JSONField(CharField):

    def __init__(self, encoder=None, decoder=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.encoder = encoder
        self.decoder = decoder

    @classmethod
    def _build_from_model_field(cls, field_instance: ModelJSONField) -> 'CharField':
        return cls(
            max_length=field_instance.max_length, choices=field_instance.choices,
            encoder=field_instance.encoder, decoder=field_instance.decoder
        )

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return JSONFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return JSONFieldMockManager(self)

    def to_python(self, value) -> Any:
        value = super().to_python(value)

        try:
            return json.loads(value, cls=self.decoder)
        except json.JSONDecodeError:
            raise ValidationError(
                ModelJSONField.default_error_messages["invalid"],
                code="invalid"
            )

    def to_json(self, value) -> str:
        return json.dumps(value, ensure_ascii=False, cls=self.encoder)

    def check_has_changed(self, old_value, new_value) -> Tuple[bool, Any, Any]:
        ov = self.to_json(old_value)
        nv = self.to_json(new_value)
        return super().check_has_changed(ov, nv)
