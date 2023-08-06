# -*- coding: utf-8 -*-
from typing import Dict, Type
from django.db import models

from a3dj.structs.base.base_field import BaseField
from a3dj.structs.fields.related_field_translater import RelatedFieldTranslater
from a3dj.structs import fields


class ModelFieldTranslater(RelatedFieldTranslater):
    cached_mappings = dict()
    mappings: Dict[Type[models.Field], Type[BaseField]] = {
        models.AutoField: fields.IntegerField,
        models.BigAutoField: fields.IntegerField,
        models.BigIntegerField: fields.IntegerField,
        models.BinaryField: fields.BinaryField,
        models.BooleanField: fields.BooleanField,
        models.CharField: fields.CharField,
        models.DateField: fields.DateField,
        models.DateTimeField: fields.DateTimeField,
        models.DecimalField: fields.DecimalField,
        models.DurationField: fields.DurationField,
        models.EmailField: fields.EmailField,
        models.FileField: fields.FileField,
        models.FilePathField: fields.CharField,
        models.FloatField: fields.FloatField,
        models.GenericIPAddressField: fields.GenericIPAddressField,
        models.ImageField: fields.ImageField,
        models.IntegerField: fields.IntegerField,
        models.JSONField: fields.JSONField,
        models.PositiveIntegerField: fields.PositiveIntegerField,
        models.PositiveBigIntegerField: fields.PositiveIntegerField,
        models.PositiveSmallIntegerField: fields.PositiveIntegerField,
        models.SlugField: fields.CharField,
        models.SmallAutoField: fields.IntegerField,
        models.SmallIntegerField: fields.IntegerField,
        models.TextField: fields.CharField,
        models.TimeField: fields.TimeField,
        models.URLField: fields.URLField,
        models.UUIDField: fields.UUIDField,
        # related
        models.ForeignKey: fields.ModelInstanceField,
        models.OneToOneField: fields.ModelInstanceField,
        models.ManyToManyField: fields.ModelMultipleInstanceField,
    }
