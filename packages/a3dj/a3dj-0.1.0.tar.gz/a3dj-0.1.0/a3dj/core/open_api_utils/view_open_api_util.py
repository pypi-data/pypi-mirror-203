# -*- coding: utf-8 -*-
from typing import Type

from a3dj.errors import Error
from a3dj.structs import json_structs
from a3dj.structs.mockers import FixedValueMocker


class ViewOpenApiUtil:

    @classmethod
    def render_empty_request_application_content(cls) -> dict:
        return {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {},
                    "x-apifox-ignore-properties": [],
                    "x-apifox-orders": []
                }
            }
        }

    @classmethod
    def render_success_response_struct(cls, s: json_structs.JsonStruct) -> dict:
        return {
            "200": {
                "description": "OK",
                "content": s.to_application_open_api_dict()
            }
        }

    @classmethod
    def render_error_response_struct(cls, err: Type[Error]) -> dict:
        class ErrorJsonStruct(json_structs.JsonStruct):
            status = json_structs.CharField(mocker=FixedValueMocker(err.__name__))
            error_message = json_structs.CharField(mocker=FixedValueMocker(str(err.default_message)))

        return {
            f'x-200:{err.__name__}': {
                "description": err.__name__,
                "content": ErrorJsonStruct.to_application_open_api_dict()
            }
        }
