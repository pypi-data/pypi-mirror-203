# -*- coding: utf-8 -*-
import copy
import json
import inspect
import os.path
from importlib import import_module
from typing import List, Dict, Type

from django.apps import AppConfig
from django.conf import settings
from django.urls import URLPattern, URLResolver
from django.utils.module_loading import import_string

from a3dj.core.inner_errors import OpenApiDocError
from a3dj.structs.json_structs.base_json_struct import BaseJsonStruct
from a3dj.errors import Error
from a3dj.view.base_post_view import BasePostView
from .view_open_api_util import ViewOpenApiUtil


def _get_cls_module_errors(cls) -> dict:
    rd = dict()

    module = import_string(cls.__module__)
    for name in dir(module):
        if name.startswith('_'):
            continue

        t = getattr(module, name)
        if inspect.isclass(t) and t is not Error and issubclass(t, Error):
            rd[t.__name__] = t
    return rd


def _get_app_name_by_urls_path(urls_path: str) -> str:
    app_path = copy.deepcopy(urls_path)

    while True:
        app_path = app_path.rsplit('.', 1)[0]
        try:
            apps_module = import_module(f'{app_path}.apps')
            for name in dir(apps_module):
                if name.startswith('_'):
                    continue

                t = getattr(apps_module, name)
                if inspect.isclass(t) and t is not AppConfig and issubclass(t, AppConfig):
                    return getattr(t, 'verbose_name', None) or getattr(t, 'name')
        except Exception as e:
            if '.' not in app_path:
                # url不在一个标准app中
                raise OpenApiDocError(f"`{urls_path}` can not find related AppConfig, {e}.")
            else:
                continue
        # app文件，但没有标准的AppConfig
        raise OpenApiDocError(f"`{urls_path}` can not find related AppConfig.")


class OpenApiDocGenerator:

    def __init__(self, project_name: str):
        self.project_name = project_name

        self._middleware_errors = dict()

        self._view_info_list = list()
        self._view2all_error_list: Dict[Type[BasePostView], List[Type[Error]]] = dict()
        self.__all_view2errors: Dict[Type[BasePostView], Dict[str, Type[Error]]] = dict()
        self._components = dict()

    def _write_doc(self, doc: dict):
        str_doc = json.dumps(doc, indent=2, ensure_ascii=False)
        filename = os.path.join(settings.BASE_DIR, f'{self.project_name}.json')
        with open(filename, 'w', encoding='utf-8') as fd:
            fd.write(str_doc)

    def _collect_errors_from_middlewares(self):
        for middleware_path in reversed(settings.MIDDLEWARE):
            middleware = import_string(middleware_path)
            errors = _get_cls_module_errors(middleware)

            self._middleware_errors.update(errors)

    def _collect_views(self):
        def _get_view_errors(vc: Type[BasePostView]):

            def __get_unit_view_errors(cls) -> dict:
                cached_errors = self.__all_view2errors.get(cls)
                if cached_errors is not None:
                    return cached_errors
                errors = _get_cls_module_errors(cls)
                self.__all_view2errors[cls] = errors
                return errors

            view_cls_errors = __get_unit_view_errors(vc)

            all_parents_errors = dict()
            for parent_cls in vc.__mro__[1:]:
                if not issubclass(parent_cls, BasePostView):
                    break
                parent_errors = __get_unit_view_errors(parent_cls)
                all_parents_errors.update(parent_errors)

            all_errors = dict()
            all_errors.update(view_cls_errors)
            all_errors.update(all_parents_errors)
            all_errors.update(self._middleware_errors)

            self._view2all_error_list[vc] = list(all_errors.values())

        def _extract_views(urlpatterns, parent_path: str = '', app_name: str = None) -> list:
            view_info_list = list()
            for p in urlpatterns:
                if isinstance(p, URLPattern):
                    callback = getattr(p, 'callback', {})
                    view_cls = getattr(callback, 'view_class', None)
                    if view_cls is not None and issubclass(view_cls, BasePostView):

                        _get_view_errors(view_cls)

                        last_path_name = str(p.pattern)
                        view_info_list.append(
                            (view_cls, parent_path + last_path_name, p.name or last_path_name, app_name)
                        )

                elif isinstance(p, URLResolver):
                    next_urlpatterns = getattr(p, 'url_patterns', None)

                    if next_urlpatterns is not None:
                        if inspect.ismodule(p.urlconf_module):
                            urls_path = p.urlconf_module.__name__
                            app_name = _get_app_name_by_urls_path(urls_path)

                        view_info_list.extend(_extract_views(next_urlpatterns, parent_path + str(p.pattern), app_name))

            return view_info_list

        urlconf = import_string(settings.ROOT_URLCONF)
        self._view_info_list = _extract_views(urlconf.urlpatterns)

    def _build_views_doc(self) -> dict:
        rd = dict()
        for view_cls, path, view_name, app_name in self._view_info_list:
            view_cls: Type[BasePostView]

            # request
            request_struct_cls = view_cls.request_struct_cls
            if request_struct_cls is None:
                request_dict = ViewOpenApiUtil.render_empty_request_application_content()
            else:
                request_dict = request_struct_cls.to_application_open_api_dict()

            # response
            response_dict = ViewOpenApiUtil.render_success_response_struct(view_cls.response_struct_cls)
            # build ordered error response
            for error in self._view2all_error_list[view_cls]:
                response_dict.update(ViewOpenApiUtil.render_error_response_struct(error))

            description = view_cls.__doc__
            if description is not None:
                description = description.strip()
            else:
                description = ''

            vd = {
                f"/{path}": {
                    "post": {
                        "summary": view_name,
                        "x-apifox-folder": app_name,
                        "deprecated": False,
                        "description": description,
                        "requestBody": {
                            "content": request_dict
                        },
                        "responses": response_dict
                    }
                }
            }
            rd.update(vd)

            if inspect.isclass(view_cls.request_struct_cls) and issubclass(view_cls.request_struct_cls, BaseJsonStruct):
                request_components = view_cls.request_struct_cls.get_open_api_components()
                self._components.update(request_components)

            if hasattr(view_cls.response_struct_cls, 'get_open_api_components'):
                response_components = view_cls.response_struct_cls.get_open_api_components()
                self._components.update(response_components)
        return rd

    def _build_components_doc(self) -> dict:
        rd = dict()
        for name, component in self._components.items():
            rd[name] = component.to_open_api_component_dict()
        return rd

    def start(self):
        self._collect_errors_from_middlewares()
        self._collect_views()

        paths = self._build_views_doc()
        components = self._build_components_doc()

        doc = {
            "openapi": "3.1.0",
            "info": {
                "title": self.project_name,
            },
            "paths": paths,
            "components": {
                'schemas': components
            }
        }

        self._write_doc(doc)
