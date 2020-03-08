# admin.py: это файл конфигурации для встроенного приложения Django под названием Django Admin.

from django.contrib import admin
from .models import Person

admin.site.register(Person)
