# -*- coding: utf-8 -*-
import logging
from django.http import HttpRequest, Http404
from django.utils.deprecation import MiddlewareMixin

from a3dj.errors import Error, SUnknownError, SKnownError
from a3dj.core.request_utils import build_critical_message
from a3dj.core.response_utils import build_error_response
from a3dj.core.inner_errors import BaseInnerError


class ExceptionMiddleware(MiddlewareMixin):
    """
    通常放在最上面，这样可以处理所有的异常

    """

    def process_exception(self, request: HttpRequest, exception: Exception):
        logger = logging.getLogger(f'a3dj.{self.__class__.__name__}')

        if isinstance(exception, Error):
            error_response = build_error_response(exception)

            if exception.status.startswith('S'):
                logger.critical(build_critical_message(request, exception))
            else:
                error_message = f'[{request.path}]-[{exception.status}]: {str(exception)};;{repr(exception)}'
                logger.info(error_message)
        elif isinstance(exception, BaseInnerError):
            error_response = build_error_response(SKnownError())
            logger.critical(build_critical_message(request, exception))
        elif isinstance(exception, Http404):
            raise exception
        else:
            error_response = build_error_response(SUnknownError())
            logger.critical(build_critical_message(request, exception))

        return error_response
