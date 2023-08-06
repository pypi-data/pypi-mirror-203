# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy as _

from .error import Error


class ServerError(Error):
    default_message = _('Server error.')


class SUnknownError(ServerError):
    default_message = _('This is a unknown logic error, please contact customer service.')


class SKnownError(ServerError):
    default_message = _('It is a known server error, please contact customer service.')
