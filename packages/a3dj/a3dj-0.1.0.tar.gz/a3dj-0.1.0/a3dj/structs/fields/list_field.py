# -*- coding: utf-8 -*-
from typing import Iterable, List

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models import ManyToManyField as ModelManyToManyField
from django.utils.translation import gettext_lazy as _

from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import ListMocker, BaseMocker
from a3dj.patches import PatchedValidationError
from a3dj.core.utils import set_meaning_kv
from a3dj.core.inner_errors import ModelFieldTranslateError


class ListFieldOpenApiManager(BaseFieldOpenApiManager):
    field: 'ListField'

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.Array

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'array'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.Array

    def _build_json_base_info(self) -> dict:
        info = super()._build_json_base_info()
        info['items'] = self.field.item_type.open_api_manager.to_json_open_api_dict()

        set_meaning_kv(info, 'minItems', self.field.min_length)
        set_meaning_kv(info, 'maxItems', self.field.max_length)
        set_meaning_kv(info, 'uniqueItems', self.field.unique)
        return info

    def get_components(self) -> dict:
        components = dict()
        sub_components = self.field.item_type.open_api_manager.get_components()
        if isinstance(sub_components, dict) and len(sub_components) > 0:
            components.update(sub_components)

        return components


class ListFieldMockManager(BaseFieldMockManager):
    field: 'ListField'

    def _preset_default_mocker(self) -> BaseMocker:
        return ListMocker(self.field.item_type, self.field.min_length, self.field.max_length, self.field.unique)


class ListField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: ModelManyToManyField) -> 'BaseField':
        raise ModelFieldTranslateError("No field can translate to ListField")

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return ListFieldOpenApiManager(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return ListFieldMockManager(self)

    default_error_messages = {
        "unique": _("“%(value)s“ already exists."),
        "invalid_type": _("This field's type must be a correct list, not “%(value)s”."),
    }

    def __init__(
            self, item_type: BaseField, min_length: int = None, max_length: int = None, unique: bool = False,
            *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.item_type = item_type

        self.min_length = min_length
        self.max_length = max_length
        self.unique = unique

        if self.min_length is not None:
            self.validators.append(MinLengthValidator(self.min_length))

        if self.max_length is not None:
            self.validators.append(MaxLengthValidator(self.max_length))

    def validate(self, value, struct_instance):
        value = super().validate(value, struct_instance)
        if self.unique and isinstance(value, Iterable):
            seen = list()
            for i, item in enumerate(value):
                if item in seen:
                    e: PatchedValidationError = ValidationError(
                        message=self.default_error_messages["unique"],
                        code="unique",
                        params={"value": str(item)},
                    )
                    e.set_index(i)
                    raise e

                seen.append(item)

        return value

    def to_python(self, value: List) -> List:
        if not isinstance(value, list):
            raise ValidationError(
                message=self.default_error_messages["invalid_type"],
                code="invalid_type",
                params={"value": type(value)}
            )

        rl = list()
        for i, item in enumerate(value):
            try:
                v = self.item_type.clean_for_python(item, None)
            except ValidationError as e:
                e: PatchedValidationError

                e.set_index(i)
                raise e
            rl.append(v)

        return rl

    def to_json(self, value: List) -> List:
        rl = list()
        for item in value:
            v = self.item_type.to_json(item)
            rl.append(v)
        return rl
