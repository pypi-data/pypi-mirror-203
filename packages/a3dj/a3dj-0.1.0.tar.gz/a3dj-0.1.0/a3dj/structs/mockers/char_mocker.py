# -*- coding: utf-8 -*-
from typing import Optional
from .base_mocker import BaseMocker


class CharMocker(BaseMocker):

    def __init__(self, min_length: int = None, max_length: int = None, choices=None):
        super().__init__()

        self._choices = None
        self._choice_index = 0
        self._min_length = None
        self._max_length = None

        if choices is not None:
            self._choices = list()
            for k, _ in choices:
                self._choices.append(k)
        else:
            if max_length is None and min_length is None:
                min_length = 5
                max_length = 15
            elif max_length is not None:
                min_length = max_length - 10
                if min_length < 1:
                    min_length = 1
            else:
                max_length = min_length + 10

            self._max_length = max_length
            self._min_length = min_length

    def mock(self, _, __) -> str:
        if self._choices is not None:
            v = self._choices[self._choice_index]
            self._choice_index += 1
            if self._choice_index >= len(self._choices):
                self._choice_index = 0
            return v

        return self.f.pystr(self._min_length, self._max_length)

    def to_json_mock_string(self) -> Optional[str]:
        if self._choices is not None:
            return f"{self._choices[0][0]}"
        return f"@string({self._min_length}, {self._max_length})"

    def to_form_mock_string(self) -> Optional[str]:
        if self._choices is not None:
            return f"{self._choices[0][0]}"
        return f"{{% mock 'string' ,  {self._min_length}, {self._max_length} %}}"
