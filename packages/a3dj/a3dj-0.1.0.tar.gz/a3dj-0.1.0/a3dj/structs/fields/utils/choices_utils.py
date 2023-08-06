# -*- coding: utf-8 -*-
from typing import List, Tuple

from django.core.exceptions import ValidationError
from django.db.models.fields import Field


def validate_choices(choices: List[Tuple], value):
    for option_key, option_value in choices:
        if value == option_key:
            return value
    raise ValidationError(
        message=Field.default_error_messages["invalid_choice"],
        code="invalid_choice",
        params={"value": value},
    )


def choices2open_api_dict(choices: List[Tuple]) -> dict:
    enum_list = list()
    enum_dict = dict()
    for option_key, option_value in choices:
        enum_list.append(option_key)
        enum_dict[option_key] = option_value

    return {
        'enum': enum_list,
        'x-apifox': {
            'enumDescriptions': enum_dict
        }
    }
