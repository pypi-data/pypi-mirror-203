# -*- coding: utf-8 -*-
import inspect
from abc import ABC
from itertools import chain
from typing import Dict, Tuple, Any, List, Type, Set
from django.db import models

from a3dj.utils.hint_utils import TypeA3Model
from a3dj.core.inner_errors import ModelStructError
from a3dj.structs.base.struct import StructMetaClass, StructOptions

from .model_field_translater import ModelFieldTranslater


class ModelStructOptions(StructOptions):
    model: Type[TypeA3Model] = None
    include: List[str] = None
    exclude: List[str] = None

    def __init__(self):
        self.m2m_field_list = list()
        self.cache_model_fields = dict()
        self.include_field_set = set()
        self.exclude_field_set = set()


class ModelStructMetaClass(StructMetaClass, ABC):

    def _get_meta(cls, meta: Type[ModelStructOptions]) -> ModelStructOptions:
        if inspect.isclass(meta) and issubclass(meta, ModelStructOptions):
            return meta()
        raise ModelStructError(f"{cls.__name__} must have correct ModelOptions")

    def _add_other_fields(cls, field_name_set: Set[str]):
        # add model fields
        meta: ModelStructOptions = cls._meta
        opts = getattr(meta.model, '_meta')
        for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
            if meta.include and f.name not in meta.include:
                meta.exclude_field_set.add(f.name)
                continue
            if meta.exclude and f.name in meta.exclude:
                meta.exclude_field_set.add(f.name)
                continue
            if f.name in field_name_set and meta.fields.get(f.name, None) is None:
                # 子类屏蔽
                meta.exclude_field_set.add(f.name)
                continue

            field_name_set.add(f.name)
            meta.include_field_set.add(f.name)
            meta.cache_model_fields[f.name] = f

            if isinstance(f, models.ManyToManyField):
                meta.m2m_field_list.append(f.name)

            # field转换
            meta.fields[f.name] = ModelFieldTranslater.translate(f)

    def _check_meta(cls):
        meta: ModelStructOptions = cls._meta

        if not inspect.isclass(meta.model) or not issubclass(meta.model, models.Model):
            raise ModelStructError(f"{cls.__name__} must set correct model, not {type(meta.model)}")

        if meta.include is not None and meta.exclude is not None:
            raise ModelStructError(f"{cls.__name__} must specify include or exclude, not both")


class ModelStructMixin:
    _meta: ModelStructOptions

    def __init__(self, instance: TypeA3Model = None):
        if instance is None:
            self.instance: TypeA3Model = self._meta.model()
            self._is_new = True
        else:
            self.instance = instance
            self._is_new = False

        self._has_save_instance: bool = False
        self._changed_data: dict = dict()

    def _apply_instance(self):
        for field_name in self._meta.include_field_set:
            model_field_instance = self._meta.cache_model_fields[field_name]
            field_instance = self._meta.fields[field_name]

            new_value = getattr(self, field_name)
            if not self._is_new:
                old_value = getattr(self.instance, field_name)

                if isinstance(model_field_instance, (models.BinaryField, models.FileField)) and \
                        not field_instance.required:
                    # update 时，不上传文件，不意味着删除
                    continue
                else:
                    if field_name in self._meta.m2m_field_list:
                        old_value = old_value.all()
                    has_changed, ov, nv = self._meta.fields[field_name].check_has_changed(old_value, new_value)
                    if has_changed:
                        self._changed_data[field_name] = (ov, nv)

            if field_name not in self._meta.m2m_field_list:
                model_field_instance.save_form_data(self.instance, new_value)

    def clean(self):
        self._apply_instance()
        self.instance.full_clean(exclude=self._meta.exclude_field_set)

    def save(self, commit=True) -> TypeA3Model:
        if commit:
            self.instance.save()
            self._save_m2m()
        self._has_save_instance = True
        return self.instance

    def _save_m2m(self):
        for field_name in self._meta.m2m_field_list:
            value = getattr(self, field_name)

            field_instance = self._meta.cache_model_fields[field_name]
            field_instance.save_form_data(self.instance, value)

    def save_m2m(self):
        if not self._has_save_instance:
            self.instance.save()
        self._save_m2m()

    def has_changed(self) -> bool:
        return len(self._changed_data) > 0

    def get_changed_data(self) -> Dict[str, Tuple[Any, Any]]:
        return self._changed_data
