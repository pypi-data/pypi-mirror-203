# -*- coding: utf-8 -*-
from a3dj.utils.hint_utils import TypeA3Model

from ..model_struct import ModelStructMetaClass, ModelStructMixin, ModelStructOptions
from .base_json_struct import BaseJsonStruct
from .json_struct import JsonStructMetaClass


ModelJsonStructOptions = ModelStructOptions


class ModelJsonStructMetaClass(ModelStructMetaClass):
    _check_field = JsonStructMetaClass._check_field # noqa


class ModelJsonStruct(BaseJsonStruct, ModelStructMixin, metaclass=ModelJsonStructMetaClass):
    _meta: ModelStructOptions

    def __init__(self, data=None, instance: TypeA3Model = None, **kwargs):
        BaseJsonStruct.__init__(self, data=data, **kwargs)
        ModelStructMixin.__init__(self, instance)

    def clean(self):
        ModelStructMixin.clean(self)
