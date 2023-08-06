# -*- coding: utf-8 -*-
from typing import Optional
from .base_mocker import BaseMocker


class IntegerMocker(BaseMocker):

    def __init__(self, min_value: int = None, max_value: int = None, choices=None):
        super().__init__()

        self._choices = None
        self._choice_index = 0
        self._min_value = None
        self._max_value = None

        if choices is not None:
            self._choices = list()
            for k, _ in choices:
                self._choices.append(k)
        else:
            if max_value is None and min_value is None:
                min_value = 500
                max_value = 1500
            elif max_value is not None:
                min_value = max_value - 500
                if max_value > 0 and min_value < 1:
                    min_value = 1
            else:
                max_value = min_value + 1000

            self._max_value = max_value
            self._min_value = min_value

    def mock(self, _, __) -> str:
        if self._choices is not None:
            v = self._choices[self._choice_index]
            self._choice_index += 1
            if self._choice_index >= len(self._choices):
                self._choice_index = 0
            return v

        return self.f.random_int(self._min_value, self._max_value)

    def to_mock_string(self) -> Optional[str]:
        if self._choices is not None:
            return
        return f"@integer({self._min_value}, {self._max_value})"

    def to_json_mock_string(self) -> Optional[str]:
        if self._choices is not None:
            return f"{self._choices[0][0]}"
        return f"@integer({self._min_value}, {self._max_value})"

    def to_form_mock_string(self) -> Optional[str]:
        if self._choices is not None:
            return f"{self._choices[0][0]}"
        return f"{{% mock 'integer' ,  {self._min_value}, {self._max_value} %}}"
