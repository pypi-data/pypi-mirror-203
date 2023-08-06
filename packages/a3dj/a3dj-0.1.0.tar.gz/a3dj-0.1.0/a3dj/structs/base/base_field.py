# -*- coding: utf-8 -*-
import abc
from typing import List, Callable, Any, Optional, Tuple

from django.core.exceptions import ValidationError
from django.forms.fields import Field as DjangoFormField
from django.db.models import Field as ModelField, NOT_PROVIDED

from a3dj.structs.mockers import BaseMocker
from a3dj.core.utils import set_meaning_kv


class FormType:
    String = "string"
    Integer = 'integer'
    Number = 'number'
    Array = 'array'
    File = 'file'


class JsonType:
    Boolean = 'boolean'
    String = 'string'
    Integer = 'integer'
    Number = 'number'
    Array = 'array'
    Object = 'object'


_HAS_DEFAULT_JSON_TYPES = (JsonType.Boolean, JsonType.String, JsonType.Integer, JsonType.Number)


class BaseFieldOpenApiManager(abc.ABC):

    def __init__(self, field: "BaseField"):
        self.field = field

    @classmethod
    @abc.abstractmethod
    def _preset_open_api_format(cls) -> str:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def _preset_json_type(cls) -> str:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def _preset_form_type(cls) -> str:
        raise NotImplementedError()

    def get_components(self) -> Optional[dict]:
        return

    def _build_json_base_info(self) -> dict:
        info = {
            'type': self._preset_json_type(),
            'format': self._preset_open_api_format(),
        }

        set_meaning_kv(info, 'title', self.field.verbose_name)
        set_meaning_kv(info, 'description', self.field.description)

        if self._preset_json_type() in _HAS_DEFAULT_JSON_TYPES and self.field.default is not None:
            if isinstance(self.field.default, Callable):
                value = self.field.default()
            else:
                value = self.field.default

            info['default'] = self.field.to_json(value)

        mock_value = self.field.mock_manager.to_json_mock_string()
        if mock_value not in [None, '']:
            info['mock'] = {
                'mock': mock_value
            }
        return info

    def _build_form_base_info(self) -> dict:
        form_type = self._preset_form_type()
        if form_type == FormType.File:
            info = {
                "type": FormType.String,
                "format": "binary"
            }
        else:
            info = {
                'type': form_type
            }

        dl = list()
        if self.field.verbose_name is not None:
            dl.append(self.field.verbose_name)
        if self.field.description not in [None, '']:
            dl.append(self.field.description)

        set_meaning_kv(info, 'description', ';'.join(dl))

        mock_value = self.field.mock_manager.to_form_mock_string()
        if mock_value not in [None, '']:
            info['example'] = mock_value
        return info

    def to_json_open_api_dict(self) -> dict:
        return self._build_json_base_info()

    def to_form_open_api_dict(self) -> dict:
        return self._build_form_base_info()


class BaseFieldMockManager(abc.ABC):

    def __init__(self, field: "BaseField"):
        self.field = field

    def mock(self, instance, root_instance) -> Any:
        mocker = self._get_mocker()
        return mocker.mock(instance, root_instance)

    def to_json_mock_string(self):
        mocker = self._get_mocker()
        return mocker.to_json_mock_string()

    def to_form_mock_string(self):
        mocker = self._get_mocker()
        return mocker.to_form_mock_string()

    def _get_mocker(self) -> BaseMocker:
        if self.field.mocker is None:
            self.field.mocker = self._preset_default_mocker()
        return self.field.mocker

    @abc.abstractmethod
    def _preset_default_mocker(self) -> BaseMocker:
        raise NotImplementedError()


class BaseField(abc.ABC):

    def __init__(
            self,
            verbose_name=None,
            description=None,
            default=None,
            required: bool = True,
            validators: List = None,
            mocker: BaseMocker = None
    ):
        self.verbose_name = verbose_name
        self.description = description or ''
        self.default = default
        self.required = required
        self.validators = validators or list()
        self.mocker = mocker

        self.open_api_manager = self._preset_open_api_manager()
        self.mock_manager = self._preset_mock_manager()

        self._struct_cls = None
        self._name = None

    def contribute_to_struct(self, struct_cls, name: str):
        self._struct_cls = struct_cls
        self._name = name

    def __str__(self) -> str:
        if self._struct_cls is None:
            return super().__str__()
        return f'{self._struct_cls}.{self._name}'

    def __repr__(self):
        path = f'{self.__class__.__module__}.{self.__class__.__qualname__}'
        if self._name is None:
            return f'<{path}>'
        return f'<{path}: {self._name}>'

    def _run_validators(self, value):
        for v in self.validators:
            v(value)

    def validate(self, value, struct_instance):
        if value is None and self.default is not None:
            if isinstance(self.default, Callable):
                value = self.default()
            else:
                value = self.default

        if value is None and self.required:
            raise ValidationError(message=DjangoFormField.default_error_messages["required"], code="required")

        return value

    def clean_for_python(self, value, struct_instance):
        value = self.validate(value, struct_instance)
        if value is None:
            return value

        value = self.to_python(value)
        self._run_validators(value)
        return value

    def clean_for_json(self, value, struct_instance):
        if value is not None:
            value = self.to_json(value)
        return value

    @classmethod
    @abc.abstractmethod
    def support_form(cls) -> bool:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def support_json(cls) -> bool:
        raise NotImplementedError()

    @classmethod
    def build_from_model_field(cls, field_instance: ModelField) -> 'BaseField':
        instance = cls._build_from_model_field(field_instance)
        instance.verbose_name = field_instance.verbose_name
        instance.description = field_instance.help_text
        instance.required = not field_instance.null

        if field_instance.default is NOT_PROVIDED:
            instance.default = None
        else:
            instance.default = field_instance.default

        return instance

    def check_has_changed(self, old_value, new_value) -> Tuple[bool, Any, Any]:
        if old_value == new_value:
            return False, None, None
        else:
            return True, old_value, new_value

    @classmethod
    @abc.abstractmethod
    def _build_from_model_field(cls, field_instance: ModelField) -> 'BaseField':
        raise NotImplementedError()

    @abc.abstractmethod
    def to_python(self, value):
        raise NotImplementedError()

    @abc.abstractmethod
    def to_json(self, value):
        raise NotImplementedError()

    @abc.abstractmethod
    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        raise NotImplementedError()

    @abc.abstractmethod
    def _preset_mock_manager(self) -> BaseFieldMockManager:
        raise NotImplementedError()

