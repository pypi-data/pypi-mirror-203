# -*- coding: utf-8 -*-
from a3dj.structs.base.base_field import BaseField
from a3dj.structs.base.struct import StructMetaClass, StructOptions
from a3dj.core.inner_errors import FieldError
from .base_json_struct import BaseJsonStruct


JsonStructOptions = StructOptions


class JsonStructMetaClass(StructMetaClass):

    def _check_field(cls, field_name, field_instance: BaseField):
        if not field_instance.support_json():
            raise FieldError(
                f"field: {field_name}, class: {field_instance.__class__.__name__}, not support json struct."
            )


class JsonStruct(BaseJsonStruct, metaclass=JsonStructMetaClass):
    pass
