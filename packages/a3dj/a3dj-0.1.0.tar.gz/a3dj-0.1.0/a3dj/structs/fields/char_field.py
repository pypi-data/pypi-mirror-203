# -*- coding: utf-8 -*-
from typing import List, Tuple
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db.models import CharField as ModelCharField

from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import CharMocker, BaseMocker
from a3dj.core.utils import set_meaning_kv

from .utils.choices_utils import validate_choices, choices2open_api_dict

TypeCharChoices = List[Tuple[str, str]]


class CharFieldOpenApiManger(BaseFieldOpenApiManager):
    field: 'CharField'

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'string'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String

    def _build_json_base_info(self) -> dict:
        info = super()._build_json_base_info()
        set_meaning_kv(info, 'minLength', self.field.min_length)
        set_meaning_kv(info, 'maxLength', self.field.max_length)
        set_meaning_kv(info, 'pattern', self.field.pattern)
        if self.field.choices is not None:
            d = choices2open_api_dict(choices=self.field.choices)
            info.update(d)

        return info


class CharFieldMockManager(BaseFieldMockManager):
    field: 'CharField'

    def _preset_default_mocker(self) -> BaseMocker:
        return CharMocker(
            min_length=self.field.min_length, max_length=self.field.max_length, choices=self.field.choices
        )


class CharField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: ModelCharField) -> 'CharField':
        return cls(max_length=field_instance.max_length, choices=field_instance.choices)

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return CharFieldOpenApiManger(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return CharFieldMockManager(self)

    def __init__(
            self, min_length: int = None, max_length: int = None, choices: TypeCharChoices = None, pattern: str = None,
            *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.min_length = min_length
        self.max_length = max_length
        self.choices = choices
        self.pattern = pattern

        if self.min_length is not None:
            self.validators.append(MinLengthValidator(self.min_length))

        if self.max_length is not None:
            self.validators.append(MaxLengthValidator(self.max_length))

        if self.pattern is not None:
            self.validators.append(RegexValidator(self.pattern))
        else:
            for v in self.validators:
                if isinstance(v, RegexValidator):
                    self.pattern = str(v.regex.pattern)

    def validate(self, value, struct_instance):
        value = super().validate(value, struct_instance)

        if self.choices is not None and value is not None:
            value = validate_choices(choices=self.choices, value=value)

        return value

    def to_python(self, value) -> str:
        if isinstance(value, str):
            return value
        else:
            return str(value)

    def to_json(self, value: str) -> str:
        return value
