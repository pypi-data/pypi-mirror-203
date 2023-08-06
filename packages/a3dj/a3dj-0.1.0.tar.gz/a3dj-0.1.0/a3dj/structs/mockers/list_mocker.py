# -*- coding: utf-8 -*-
from typing import List
from django.utils.translation import gettext_lazy as _
from a3dj.core.inner_errors import MockError

from .base_mocker import BaseMocker


class ListMocker(BaseMocker):
    default_error_messages = {
        "NotEnough": _("Can not fake enough items, min length is %(min_length)s, current list %(str_list)s."),
    }

    def __init__(self, item_type, min_length: int = None, max_length: int = None, unique: bool = False):
        super().__init__()

        self.item_type = item_type
        self.unique = unique

        self._min_length = 1
        self._max_length = 3

        if min_length is not None and min_length > self._min_length:
            self._min_length = min_length
            self._max_length = self._min_length + 2

        if max_length is not None and max_length < self._max_length:
            self._max_length = max_length

    def mock(self, instance, root_instance) -> List:
        length = self.f.random_int(self._min_length, self._max_length)
        rl = list()
        for i in range(length):
            v = self.item_type.mock_manager.mock(instance=instance, root_instance=root_instance)
            if self.unique and v in rl:
                continue

            rl.append(v)
        if len(rl) < self._min_length:
            raise MockError(
                error_message=self.default_error_messages['NotEnough'],
                params={
                    'min_length': self._min_length,
                    'str_list': str(rl)
                }
            )
        return rl

    def to_json_mock_string(self):
        return

    def to_form_mock_string(self):
        v = self.item_type.mock_manager.to_form_mock_string()
        if v not in ['', None]:
            return [v, ]
