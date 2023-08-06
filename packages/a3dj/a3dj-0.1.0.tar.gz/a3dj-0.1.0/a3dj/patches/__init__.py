# -*- coding: utf-8 -*-
from .patch_validation_error import PatchedValidationError, _patch_validation_error


def monkey_patch():
    _patch_validation_error()
