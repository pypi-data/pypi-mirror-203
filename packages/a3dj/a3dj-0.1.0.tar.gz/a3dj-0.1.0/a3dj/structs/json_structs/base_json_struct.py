# -*- coding: utf-8 -*-
from typing import Type

from a3dj.structs.base.struct import Struct


class BaseJsonStruct(Struct):

    @classmethod
    def to_application_open_api_dict(cls) -> dict:
        return {
            'application/json': {
                "schema": cls.to_json_open_api_dict()
            }
        }

    @classmethod
    def to_json_open_api_dict(cls) -> dict:
        if cls.is_open_api_component():
            rd = {
                "$ref": f"#/components/schemas/{cls.__name__}"
            }
        else:
            rd = cls.to_open_api_component_dict()

        return rd

    @classmethod
    def is_open_api_component(cls) -> bool:
        return cls._meta.is_component

    @classmethod
    def to_open_api_component_dict(cls) -> dict:
        order_list = list()
        required_list = list()
        properties = dict()

        for field_name, field_instance in cls._meta.fields.items():
            order_list.append(field_name)

            if field_instance.required:
                required_list.append(field_name)

            properties[field_name] = field_instance.open_api_manager.to_json_open_api_dict()

        return {
            'type': 'object',
            'properties': properties,
            'required': required_list,
            'x-apifox-orders': order_list
        }

    @classmethod
    def get_open_api_components(cls) -> dict[str, Type['BaseJsonStruct']]:
        components = dict()
        if cls.is_open_api_component():
            components[cls.__name__] = cls
        else:
            for _, field_instance in cls.get_meta().fields.items():
                sub_components = field_instance.open_api_manager.get_components()
                if isinstance(sub_components, dict) and len(sub_components) > 0:
                    components.update(sub_components)

        return components
