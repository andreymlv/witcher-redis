# models.py: здесь мы определяем сущности нашего веб-приложения.

from django.db import models

# Create your models here.


class Person(models.Model):
    """Модель перонажа"""
    # Идентификатор (число, не может повторятся)
    identifier = models.IntegerField(verbose_name="Идентификатор")
    # Имя (текст)
    name = models.CharField(
        verbose_name="Имя",
        max_length=100
    )
    # Должность (текст, не обязательное)
    post = models.CharField(
        verbose_name="Должность",
        max_length=100,
        blank=True,
        null=True
    )
    # URL фотографии
    # (текстом, изображения берутся из общей папки)
    image = models.CharField(
        verbose_name="URL фотографии",
        max_length=100
    )
    # Идентификатор начальника, кому подчиняется
    # (число, если отсутствует — это самый верхний уровень)
    parent_id = models.IntegerField(
        verbose_name="Идентификатор начальника",
        blank=True,
        null=True
    )

    def __str__(self):
        """Если к объекту обращаются в виде строки, то возвращается имя объекта"""
        return self.name
