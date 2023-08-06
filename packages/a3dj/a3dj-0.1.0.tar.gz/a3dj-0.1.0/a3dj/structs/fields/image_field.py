# -*- coding: utf-8 -*-
from a3dj.core.validators import ImageFileValidator

from .file_field import FileField


class ImageField(FileField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(ImageFileValidator())
