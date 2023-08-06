# -*- coding: utf-8 -*-
import abc


class BaseRequestPermission(abc.ABC):

    @abc.abstractmethod
    def __call__(self, request):
        raise NotImplementedError()
