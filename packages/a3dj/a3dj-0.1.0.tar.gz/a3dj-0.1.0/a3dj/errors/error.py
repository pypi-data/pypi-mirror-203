# -*- coding: utf-8 -*-


class Error(Exception):
    default_message = 'error'

    def __init__(self, error_message: str = None, detail_message: str = None):
        self.status = self.__class__.__name__
        self.error_message = error_message or self.default_message
        self.default_message = detail_message or ''

    def __str__(self):
        return f"{self.error_message}"

    def __repr__(self):
        return f"{self.default_message}"
