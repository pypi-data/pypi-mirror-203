# -*- coding: utf-8 -*-
import base64
from typing import Any, Tuple

from django.core.exceptions import ValidationError
from django.db.models import FileField as ModelFileField
from django.forms import FileField as DjangoFormFileField
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db.models.fields.files import FieldFile

from a3dj.core.validators import FileMaxSizeValidator
from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import NoneMocker, BaseMocker


class FileFieldOpenApiManger(BaseFieldOpenApiManager):
    field: 'FileField'

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.File

    @classmethod
    def _preset_open_api_format(cls) -> str:
        # 通过Json传来的，只能是base64
        return 'base64'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String


class FileFieldMockManager(BaseFieldMockManager):
    field: 'FileField'

    def _preset_default_mocker(self) -> BaseMocker:
        return NoneMocker()


class FileField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: ModelFileField) -> 'FileField':
        return cls(max_length=field_instance.max_length)

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return FileFieldOpenApiManger(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return FileFieldMockManager(self)

    def __init__(self, max_length: int = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.max_length = max_length
        if self.max_length is not None:
            self.validators.append(FileMaxSizeValidator(self.max_length))

    def to_python(self, value) -> File:
        if isinstance(value, File):
            return value

        if isinstance(value, str):
            body = base64.b64decode(value.encode("ascii"))

            temp_file = NamedTemporaryFile()
            temp_file.write(body)
            temp_file.flush()

            return File(file=temp_file)

        raise ValidationError(DjangoFormFileField.default_error_messages["invalid"], code="invalid")

    def to_json(self, value: FieldFile) -> str:
        return value.url

    def check_has_changed(self, old_value: FieldFile, new_value: FieldFile) -> Tuple[bool, Any, Any]:
        return True, str(old_value), str(new_value)
