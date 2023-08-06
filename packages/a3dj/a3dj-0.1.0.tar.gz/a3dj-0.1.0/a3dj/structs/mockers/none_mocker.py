# -*- coding: utf-8 -*-
from typing import Optional

from .base_mocker import BaseMocker


class NoneMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return

    def to_form_mock_string(self) -> Optional[str]:
        return

    def mock(self, _, __):
        return
