# -*- coding: utf-8 -*-
from typing import Optional

from .base_mocker import BaseMocker


class GenericIPAddressMocker(BaseMocker):

    def __init__(self, protocol: str = 'both'):
        super().__init__()
        self.protocol = protocol

    def to_json_mock_string(self) -> Optional[str]:
        return "@ip"

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'ip' %}"

    def mock(self, _, __) -> str:
        if self.protocol == 'ipv6':
            return self.f.ipv6()
        else:
            return self.f.ipv4()
