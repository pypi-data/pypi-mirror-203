# -*- coding: utf-8 -*-
from typing import Optional

from .base_mocker import BaseMocker


class EmailMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return "@email"

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'email' %}"

    def mock(self, _, __) -> str:
        return self.f.email()
