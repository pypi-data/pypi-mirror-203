# -*- coding: utf-8 -*-
from typing import Tuple, Any, Type
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from a3dj.utils.hint_utils import TypeA3Model
from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager
from .related_field_translater import RelatedFieldTranslater


class ModelInstanceField(BaseField):
    default_error_messages = {
        'not_exist': _("Model instance “%(value)s“ does not exist")
    }

    def __init__(
            self, model_cls: Type[TypeA3Model], to_field_name: str = None, query: dict = None,
            *args, **kwargs
    ):
        self.model_cls = model_cls
        self.to_field_name = to_field_name or 'id'
        self.query = query or dict()
        field_instance = getattr(model_cls, '_meta').get_field(self.to_field_name)
        self.outward_field: BaseField = RelatedFieldTranslater.translate(field_instance)

        super().__init__(*args, **kwargs)

    @classmethod
    def _build_from_model_field(cls, field_instance: models.ForeignKey) -> 'ModelInstanceField':
        return cls(model_cls=field_instance.related_model, to_field_name=field_instance.target_field.name)

    def to_python(self, value):
        v = self.outward_field.to_python(value)
        fd = {self.to_field_name: v}
        fd.update(self.query)

        instance = self.model_cls.objects.filter(**fd).first()
        if instance is None:
            raise ValidationError(
                message=self.default_error_messages["not_exist"],
                code="not_exist",
                params={"value": value}
            )

        return instance

    def check_has_changed(self, old_value, new_value) -> Tuple[bool, Any, Any]:
        ov = getattr(old_value, self.to_field_name, None)
        nv = getattr(new_value, self.to_field_name, None)
        if ov == nv:
            return False, None, None
        else:
            return True, ov, nv

    def to_json(self, value):
        return getattr(value, self.to_field_name, None)

    def _preset_open_api_manager(self) -> BaseFieldOpenApiManager:
        return self.outward_field.open_api_manager

    def _preset_mock_manager(self) -> BaseFieldMockManager:
        return self.outward_field.mock_manager

    @classmethod
    def support_json(cls) -> bool:
        return True

    @classmethod
    def support_form(cls) -> bool:
        return True
