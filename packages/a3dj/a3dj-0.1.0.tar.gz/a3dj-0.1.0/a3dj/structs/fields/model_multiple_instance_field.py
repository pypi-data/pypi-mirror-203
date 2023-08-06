# -*- coding: utf-8 -*-
from typing import Tuple, Any, Type
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from a3dj.utils.hint_utils import TypeA3Model
from a3dj.structs.base.base_field import BaseField, BaseFieldMockManager, BaseFieldOpenApiManager
from .list_field import ListField
from .related_field_translater import RelatedFieldTranslater
from .model_instance_field import ModelInstanceField


class ModelMultipleInstanceField(ModelInstanceField):
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
        item_type = RelatedFieldTranslater.translate(field_instance)
        self.outward_field: BaseField = ListField(item_type=item_type, required=False, unique=True)

        BaseField.__init__(self, *args, **kwargs)

    def to_python(self, value):
        vl = self.outward_field.to_python(value)
        fd = {f"{self.to_field_name}__in": vl}
        fd.update(self.query)

        instance_list = self.model_cls.objects.filter(**fd)
        if len(instance_list) != len(vl):
            cl = list()
            for instance in instance_list:
                cl.append(getattr(instance, self.to_field_name))

            raise ValidationError(
                message=self.default_error_messages["not_exist"],
                code="not_exist",
                params={"value": ','.join(list(set(vl) - set(cl)))}
            )

        return instance_list

    def check_has_changed(self, old_value, new_value) -> Tuple[bool, Any, Any]:
        ovl = list()
        for old in old_value or list():
            o = getattr(old, self.to_field_name)
            ovl.append(o)

        nvl = list()
        for ne in new_value or list():
            n = getattr(ne, self.to_field_name)
            nvl.append(n)

        if set(ovl) == set(nvl):
            return False, None, None
        else:
            return True, ovl, nvl

    def to_json(self, value):
        rl = list()
        for v in value.all():
            rl.append(getattr(v, self.to_field_name))
        return rl

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
