# -*- coding: utf-8 -*-
from a3dj.utils.hint_utils import TypeA3Model

from ..model_struct import ModelStructMetaClass, ModelStructMixin, ModelStructOptions
from .base_form_struct import BaseFormStruct
from .form_struct import FormStructMetaClass


ModelFormStructOptions = ModelStructOptions


class ModelFormStructMetaClass(ModelStructMetaClass):
    _check_field = FormStructMetaClass._check_field # noqa


class ModelFormStruct(BaseFormStruct, ModelStructMixin, metaclass=ModelFormStructMetaClass):
    _meta: ModelStructOptions

    def __init__(self, data=None, instance: TypeA3Model = None, **kwargs):
        BaseFormStruct.__init__(self, data=data, **kwargs)
        ModelStructMixin.__init__(self, instance)

    def clean(self):
        ModelStructMixin.clean(self)
