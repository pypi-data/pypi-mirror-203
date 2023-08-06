# -*- coding: utf-8 -*-
from django.http import JsonResponse

from a3dj.errors import Error


def build_success_response(data: dict = None):
    success_result = {
        'status': 'OK'
    }

    if data is not None:
        success_result['data'] = data
    return JsonResponse(data=success_result)


def build_error_response(e: Error):
    return JsonResponse(data={
        'status': e.status,
        'error_message': str(e)
    })


class FileResponseStruct:

    @classmethod
    def to_application_open_api_dict(cls):
        # 这个导入Apifox时不能正确显示，是Apifox的锅
        return {
            "application/octet-stream": {
                "schema": {
                    "type": "string",
                    "format": "binary"
                }
            }
        }
