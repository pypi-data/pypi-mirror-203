# -*- coding: utf-8 -*-
from typing import Optional

from .base_mocker import BaseMocker


class BooleanMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return "@boolean"

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'boolean' %}"

    def mock(self, _, __) -> bool:
        return self.f.boolean()
