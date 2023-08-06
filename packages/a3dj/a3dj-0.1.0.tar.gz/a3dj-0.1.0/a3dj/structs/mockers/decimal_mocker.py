# -*- coding: utf-8 -*-
from decimal import Decimal
from typing import Optional

from .base_mocker import BaseMocker


class DecimalMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return "@float"

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'float' %}"

    def mock(self, _, __) -> Decimal:
        return self.f.pydecimal()
