# -*- coding: utf-8 -*-
import base64
import hashlib
from typing import Tuple, Any

from django.db.models import BinaryField as ModelBinaryField

from a3dj.core.utils import set_meaning_kv
from a3dj.core.validators import FileMaxSizeValidator
from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager, JsonType, FormType
from a3dj.structs.mockers import NoneMocker, BaseMocker


class BinaryFieldOpenApiManger(BaseFieldOpenApiManager):
    field: 'BinaryField'

    @classmethod
    def _preset_form_type(cls) -> str:
        return FormType.String

    @classmethod
    def _preset_open_api_format(cls) -> str:
        return 'base64'

    @classmethod
    def _preset_json_type(cls) -> str:
        return JsonType.String

    def _build_json_base_info(self) -> dict:
        info = super()._build_json_base_info()
        set_meaning_kv(info, 'maxLength', self.field.max_length)

        return info


class BinaryFieldMockManager(BaseFieldMockManager):
    field: 'BinaryField'

    def _preset_default_mocker(self) -> BaseMocker:
        return NoneMocker()


class BinaryField(BaseField):

    @classmethod
    def support_form(cls) -> bool:
        return True

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def _build_from_model_field(cls, field_instance: ModelBinaryField) -> 'BinaryField':
        return cls(max_length=field_instance.max_length)

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return BinaryFieldOpenApiManger(self)

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return BinaryFieldMockManager(self)

    def __init__(self, max_length: int = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_length = max_length

        if self.max_length is not None:
            self.validators.append(FileMaxSizeValidator(self.max_length))

    def to_python(self, value) -> memoryview:
        if isinstance(value, memoryview):
            return value
        elif isinstance(value, (bytes, bytearray)):
            return memoryview(value)

        return memoryview(base64.b64decode(str(value).encode("ascii")))

    def to_json(self, value: memoryview) -> str:
        return base64.b64encode(value).decode("ascii")

    def check_has_changed(self, old_value: memoryview, new_value: memoryview) -> Tuple[bool, Any, Any]:
        def _get_md5(v) -> str:
            md5 = hashlib.md5()
            md5.update(v)
            return md5.hexdigest()

        if old_value is None:
            o = None
        else:
            o = _get_md5(old_value)

        if new_value is None:
            n = None
        else:
            n = _get_md5(new_value)
        return super().check_has_changed(o, n)
