# -*- coding: utf-8 -*-
from typing import Optional

from .base_mocker import BaseMocker


class FixedValueMocker(BaseMocker):

    def __init__(self, fixed_value):
        super().__init__()
        self.fixed_value = fixed_value

    def mock(self, _, __):
        return self.fixed_value

    def to_json_mock_string(self) -> Optional[str]:
        return f"{self.fixed_value}"

    def to_form_mock_string(self) -> Optional[str]:
        return f"{self.fixed_value}"
