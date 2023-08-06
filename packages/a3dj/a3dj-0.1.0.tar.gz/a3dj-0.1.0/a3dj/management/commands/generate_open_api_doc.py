# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings

from a3dj.core.open_api_utils import OpenApiDocGenerator


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--project-name', '-n', dest='project_name', required=False, type=str)

    def handle(self, *args, **options):
        project_name = options.pop('project_name')
        if project_name is None:
            project_name = settings.BASE_DIR.name

        OpenApiDocGenerator(project_name=project_name).start()
