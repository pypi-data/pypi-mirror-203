# -*- coding: utf-8 -*-
from typing import TypeVar

from django.db import models


class A3Model(models.Model):
    objects: models.QuerySet
    id: int

    class Meta:
        abstract = True


TypeA3Model = TypeVar('TypeA3Model', bound=A3Model)
