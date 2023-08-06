# -*- coding: utf-8 -*-
import tempfile
import json
from typing import List, Type, Dict

from django.http import JsonResponse, FileResponse
from django.test import TestCase as DjangoTestCase
from a3faker import FakerProxy

from a3dj.core.constant import RequestContentType
from a3dj import errors


class TestCase(DjangoTestCase):
    _custom_errors: Dict[str, Type[errors.Error]]
    custom_error_class_list: List[Type[errors.Error]] = list()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._custom_errors = dict()
        for error_class in cls.custom_error_class_list:
            cls._custom_errors[error_class.__name__] = error_class

    def post_json(
            self,
            path: str,
            data: dict = None,
            post_kwargs: dict = None
    ) -> dict:
        post_kwargs = post_kwargs or dict()
        post_kwargs['content_type'] = RequestContentType.Json

        return self._post(
            path=path,
            data=json.dumps(data),
            post_kwargs=post_kwargs
        )

    def post_json_return_file(
            self,
            path: str,
            data: dict = None,
            post_kwargs: dict = None,
            file_extension: str = None,
            file_kwargs: dict = None
    ) -> tempfile.NamedTemporaryFile:
        post_kwargs = post_kwargs or dict()
        post_kwargs['content_type'] = RequestContentType.Json

        return self._post(
            path=path,
            data=json.dumps(data),
            post_kwargs=post_kwargs,
            file_extension=file_extension,
            file_kwargs=file_kwargs
        )

    def post_form(
            self,
            path: str,
            data: dict = None,
            post_kwargs: dict = None
    ) -> dict:
        return self._post(
            path=path,
            data=data,
            post_kwargs=post_kwargs
        )

    def post_form_return_file(
            self,
            path: str,
            data: dict = None,
            post_kwargs: dict = None,
            file_extension: str = None,
            file_kwargs: dict = None
    ) -> tempfile.NamedTemporaryFile:
        return self._post(
            path=path,
            data=data,
            post_kwargs=post_kwargs,
            file_extension=file_extension,
            file_kwargs=file_kwargs
        )

    def _post(
            self,
            path: str,
            data=None,
            file_extension: str = None,
            post_kwargs: dict = None,
            file_kwargs: dict = None
    ):
        post_kwargs = post_kwargs or {}
        file_kwargs = file_kwargs or {}
        if file_extension is not None:
            file_kwargs['suffix'] = f'.{file_extension}'

        response = self.client.post(path, data=data, **post_kwargs)
        assert response.status_code == 200

        if isinstance(response, JsonResponse):
            rd: dict = response.json()  # noqa
            status = rd.pop('status')
            if status == 'OK':
                return rd.get('data')
            else:
                error_cls = self._custom_errors.get(status, None)
                if error_cls is None:
                    error_cls = getattr(errors, status, None)
                    assert error_cls is not None

                # 临时切一下，以方便Error子类构造函数重写
                _init = error_cls.__init__  # noqa
                error_cls.__init__ = errors.Error.__init__  # noqa
                e = error_cls(**rd)
                error_cls.__init__ = _init  # noqa
                raise e
        elif isinstance(response, FileResponse):
            tf = tempfile.NamedTemporaryFile('wb', **file_kwargs)
            for content in response.streaming_content:
                tf.write(content)
            tf.flush()

            return tf

    def setUp(self) -> None:
        super().setUp()
        self.f = FakerProxy.get_faker()
