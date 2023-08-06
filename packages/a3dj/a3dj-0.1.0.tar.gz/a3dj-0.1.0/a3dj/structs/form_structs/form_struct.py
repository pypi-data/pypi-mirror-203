# -*- coding: utf-8 -*-
from a3dj.structs.base.base_field import BaseField
from a3dj.structs.base.struct import StructMetaClass, StructOptions
from a3dj.structs.fields import ListField, ObjectField
from a3dj.core.inner_errors import FieldError

from .base_form_struct import BaseFormStruct


FormStructOptions = StructOptions


class FormStructMetaClass(StructMetaClass):

    def _check_field(cls, field_name, field_instance: BaseField):
        if not field_instance.support_form():
            raise FieldError(
                f"field: {field_name}, class: {field_instance.__class__.__name__}, not support form struct."
            )
        if isinstance(field_instance, ListField) and \
                isinstance(field_instance.item_type, (ListField, ObjectField)):
            raise FieldError(
                f"list field: {field_name}, not support item class: {field_instance.item_type.__class__.__name__}"
            )


class FormStruct(BaseFormStruct, metaclass=FormStructMetaClass):
    pass
