# -*- coding: utf-8 -*-
import uuid
from typing import Optional

from .base_mocker import BaseMocker


class UUIDMocker(BaseMocker):

    def to_json_mock_string(self) -> Optional[str]:
        return "@uuid"

    def to_form_mock_string(self) -> Optional[str]:
        return "{% mock 'uuid' %}"

    def mock(self, _, __) -> uuid.UUID:
        return uuid.uuid4()
