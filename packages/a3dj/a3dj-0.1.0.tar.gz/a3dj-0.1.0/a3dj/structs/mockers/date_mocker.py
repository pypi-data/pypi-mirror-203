# -*- coding: utf-8 -*-
import datetime
from typing import Optional

from .base_mocker import BaseMocker


class DateMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return "@date"

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'date' %}"

    def mock(self, _, __) -> datetime.date:
        return self.f.date()
