'''
Команда для импорта в БД данных об игредиентах и тегах.
Вызовается из папки "ифслутв": python manage.py import_from_csv
'''

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient, Tag


class Command(BaseCommand):

    def handle(self, **kwargs):
        with open(
            os.path.join(settings.BASE_DIR, 'data/ingredients.csv'),
            'r',
            encoding='UTF-8',
        ) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                Ingredient.objects.get_or_create(
                    name=row[0],
                    measurement_unit=row[1],
                )
        with open(
            os.path.join(settings.BASE_DIR, 'data/tags.csv'),
            'r',
            encoding='UTF-8',
        ) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                Tag.objects.get_or_create(
                    name=row[0],
                    color=row[1],
                    slug=row[2],
                )
        self.stdout.write(
            self.style.SUCCESS('ингредиенты и теги загружены')
        )
