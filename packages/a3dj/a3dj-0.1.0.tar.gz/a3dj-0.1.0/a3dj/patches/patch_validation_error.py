# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from typing import Union


__raw_str__ = ValidationError.__str__


class _PatchedValidationError:
    error_list: list
    index_list: list
    message: str
    params: dict

    def _check_has_patched(self) -> bool:
        return getattr(self, '_has_patched', False)

    def _ensure_instance_member(self):
        has_patched = self._check_has_patched()
        if not has_patched:
            self._has_patched = True
            self.index_list = list()
            self.field_name_list = list()

    def set_field(self, field_name: str):
        self._ensure_instance_member()

        if len(self.index_list) > 0:
            for index in self.index_list:
                field_name += f'[{index}]'
            self.index_list = list()

        self.field_name_list.insert(0, field_name)

    def set_index(self, index: int):
        self._ensure_instance_member()
        self.index_list.insert(0, index)

    def _patched_str(self) -> str:
        if len(self.field_name_list) == 0:
            field_name = NON_FIELD_ERRORS
        else:
            field_name = '.'.join(self.field_name_list)
        error_message = self.message
        if self.params:
            error_message %= self.params
        return f'{field_name}: {error_message}'

    def __str__(self):
        if self._check_has_patched():
            return self._patched_str()
        else:
            if hasattr(self, "error_dict"):
                field = next(iter(self.error_dict))
                error_message = str(self.error_dict[field][0])
                return f'{field}: {error_message}'
            else:
                error = self.error_list[0]
                error_message = error.message
                if error.params:
                    error_message %= error.params
                return error_message


def _patch_validation_error():
    ValidationError._check_has_patched = _PatchedValidationError._check_has_patched # noqa
    ValidationError._ensure_instance_member = _PatchedValidationError._ensure_instance_member # noqa
    ValidationError.set_field = _PatchedValidationError.set_field
    ValidationError.set_index = _PatchedValidationError.set_index
    ValidationError._patched_str = _PatchedValidationError._patched_str # noqa
    ValidationError.__str__ = _PatchedValidationError.__str__


PatchedValidationError = Union[ValidationError, _PatchedValidationError]
