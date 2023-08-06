# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy as _

from .error import Error


class ClientError(Error):
    default_message = _('Client error.')


class CRequestStructError(ClientError):
    default_message = _('The requested data structure is not in the correct format.')
