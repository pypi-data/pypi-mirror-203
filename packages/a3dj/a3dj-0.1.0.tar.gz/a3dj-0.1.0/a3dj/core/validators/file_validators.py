# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.core.files import File
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible

from a3dj.utils.media_utils import PillowImage
from a3py.improved.readable import get_readable_size


@deconstructible
class FileMaxSizeValidator:
    messages = {
        "invalid": _("File max size must less than %(value)s.")
    }

    def __init__(self, max_length: int):
        self.max_length = max_length
        self._readable_size = get_readable_size(self.max_length)

    def __call__(self, f: File):
        if len(f) > self.max_length:
            raise ValidationError(
                self.messages["invalid"], code="invalid", params={"value": self._readable_size}
            )


@deconstructible
class ImageFileValidator:
    messages = {
        "invalid": _("It is not a valid image.")
    }

    def __call__(self, f: File):
        try:
            img = PillowImage(file=f)
            f.image = img.image
            f.content_type = img.get_content_type()
        except Exception as _:
            raise ValidationError(
                self.messages["invalid"], code="invalid"
            )
