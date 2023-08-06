# -*- coding: utf-8 -*-
import datetime
from typing import Optional

from .base_mocker import BaseMocker


class DateTimeMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return "@datetime"

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'datetime' %}"

    def mock(self, _, __) -> datetime.datetime:
        return self.f.date_time()
