# -*- coding: utf-8 -*-
import abc
from collections import defaultdict
from typing import Optional

from a3faker import FakerProxy

_GlobalSequenceDict = defaultdict(int)


class BaseMocker(abc.ABC):

    def __init__(self):
        self.f = FakerProxy.get_faker()
        self._gsd = _GlobalSequenceDict
        self._cls_name = self.__class__.__name__

    def _get_sequence_index(self) -> int:
        self._gsd[self._cls_name] += 1
        return self._gsd[self._cls_name]

    @abc.abstractmethod
    def to_json_mock_string(self) -> Optional[str]:
        raise NotImplementedError()

    @abc.abstractmethod
    def to_form_mock_string(self) -> Optional[str]:
        raise NotImplementedError()

    @abc.abstractmethod
    def mock(self, instance, root_instance):
        # 用于单元测试时mock http的request
        raise NotImplementedError()
