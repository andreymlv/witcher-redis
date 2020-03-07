# admin.py: это файл конфигурации для встроенного приложения Django под названием Django Admin.

from django.contrib import admin
from .models import Person

# Register your models here.

admin.site.register(Person)
