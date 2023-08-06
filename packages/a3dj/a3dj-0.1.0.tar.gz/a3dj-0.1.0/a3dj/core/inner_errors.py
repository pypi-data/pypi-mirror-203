# -*- coding: utf-8 -*-

class BaseInnerError(Exception):

    def __init__(
            self,
            error_message: str,
            params: dict = None,
    ):
        if params:
            error_message %= params

        self.error_message = error_message

    def __str__(self):
        return f'{self.error_message}'

    def __repr__(self):
        return f"{self.__class__.__name__}: <{self}>"


class MockError(BaseInnerError):
    pass


class FieldError(BaseInnerError):
    pass


class ModelStructError(BaseInnerError):
    pass


class ModelFieldTranslateError(BaseInnerError):
    pass


class ViewError(BaseInnerError):
    pass


class OpenApiDocError(BaseInnerError):
    pass


class MixingError(BaseInnerError):
    pass
