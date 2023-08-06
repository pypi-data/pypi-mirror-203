# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from a3dj.core.factory_utils.factory_generator import FactoryGenerator


class Command(BaseCommand):

    def handle(self, *args, **options):
        FactoryGenerator().start()
