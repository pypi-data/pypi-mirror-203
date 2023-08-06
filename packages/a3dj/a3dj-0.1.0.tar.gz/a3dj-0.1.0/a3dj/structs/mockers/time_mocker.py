# -*- coding: utf-8 -*-
import datetime
from typing import Optional

from .base_mocker import BaseMocker


class TimeMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return "@time"

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'time' %}"

    def mock(self, _, __) -> datetime.time:
        return self.f.time()
