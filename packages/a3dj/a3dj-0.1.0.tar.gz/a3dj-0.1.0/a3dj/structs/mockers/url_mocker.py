# -*- coding: utf-8 -*-
from typing import Optional

from .base_mocker import BaseMocker


class URLMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return '@url("http")'

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'url' , 'http' %}"

    def mock(self, _, __) -> str:
        return self.f.url()
