# -*- coding: utf-8 -*-
import datetime
from typing import Optional

from .base_mocker import BaseMocker


class DurationMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return "@date"

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'date' %}"

    def mock(self, _, __) -> datetime.timedelta:
        first = self.f.date_time_this_year(before_now=False, after_now=True)
        second = self.f.date_time_this_year(before_now=True, after_now=False)
        return first - second
