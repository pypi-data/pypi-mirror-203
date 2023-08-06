# -*- coding: utf-8 -*-
from .base_mocker import BaseMocker


class ObjectMocker(BaseMocker):

    def __init__(self, obj_cls):
        super().__init__()
        self.obj_cls = obj_cls

    def mock(self, instance, root_instance):
        return self.obj_cls.mock(instance=instance, root_instance=root_instance)

    def to_json_mock_string(self):
        return

    def to_form_mock_string(self):
        return
