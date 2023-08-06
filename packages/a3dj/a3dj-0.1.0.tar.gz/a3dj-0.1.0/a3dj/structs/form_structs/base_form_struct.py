# -*- coding: utf-8 -*-
from a3dj.structs.base.struct import Struct


class BaseFormStruct(Struct):

    @classmethod
    def to_application_open_api_dict(cls) -> dict:
        return {
            'multipart/form-data': {
                "schema": cls.to_form_open_api_dict()
            }
        }

    @classmethod
    def to_form_open_api_dict(cls) -> dict:
        order_list = list()
        required_list = list()
        properties = dict()

        for field_name, field_instance in cls._meta.fields.items():
            order_list.append(field_name)

            if field_instance.required:
                required_list.append(field_name)

            properties[field_name] = field_instance.open_api_manager.to_form_open_api_dict()

        return {
            'type': 'object',
            'properties': properties,
            'required': required_list,
            'x-apifox-orders': order_list
        }
