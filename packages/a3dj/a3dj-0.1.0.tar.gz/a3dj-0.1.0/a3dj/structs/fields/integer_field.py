# -*- coding: utf-8 -*-
from typing import List, Tuple

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import IntegerField as ModelIntegerField

from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import IntegerMocker, BaseMocker
from a3dj.core.utils import set_meaning_kv

from .utils.choices_utils import validate_choices, choices2open_api_dict


TypeIntegerChoices = List[Tuple[int, str]]


class IntegerFieldOpenApiManager(BaseFieldOpenApiManager):
    field: 'IntegerField'

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.Integer

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'long'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.Integer

    def _build_json_base_info(self) -> dict:
        info = super()._build_json_base_info()
        set_meaning_kv(info, 'minimum', self.field.min_value)
        set_meaning_kv(info, 'maximum', self.field.max_value)

        if self.field.choices is not None:
            d = choices2open_api_dict(choices=self.field.choices)
            info.update(d)

        return info


class IntegerFieldMockManager(BaseFieldMockManager):
    field: 'IntegerField'

    def _preset_default_mocker(self) -> BaseMocker:
        return IntegerMocker(
            min_value=self.field.min_value, max_value=self.field.max_value, choices=self.field.choices
        )


class IntegerField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: ModelIntegerField) -> 'IntegerField':
        return cls(choices=field_instance.choices)

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return IntegerFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return IntegerFieldMockManager(self)

    def __init__(
            self, min_value: int = None, max_value: int = None, choices: TypeIntegerChoices = None, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.min_value = min_value
        self.max_value = max_value
        self.choices = choices

        if self.min_value is not None:
            self.validators.append(MinValueValidator(self.min_value))

        if self.max_value is not None:
            self.validators.append(MaxValueValidator(self.max_value))

    def validate(self, value, struct_instance):
        value = super().validate(value, struct_instance)

        if self.choices is not None and value is not None:
            value = validate_choices(choices=self.choices, value=value)

        return value

    def to_python(self, value) -> int:
        if isinstance(value, int):
            return value

        try:
            return int(value)
        except (TypeError, ValueError):
            raise ValidationError(
                message=ModelIntegerField.default_error_messages["invalid"],
                code="invalid",
                params={"value": value},
            )

    def to_json(self, value: int) -> int:
        return value
