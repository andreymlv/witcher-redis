# models.py: здесь мы определяем сущности нашего веб-приложения.

from django.db import models


class Person(models.Model):
    """Модель персонажа"""

    # Поле начальства
    chief = models.ForeignKey(
        'tree.Person',
        related_name='person',
        on_delete=models.CASCADE,
        verbose_name="Начальник",
        blank=True,
        null=True
    )
    # Идентификатор (число, не может повторятся)
    id = models.IntegerField(
        verbose_name="Идентификатор",
        primary_key=True
    )
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
    parent = models.IntegerField(
        verbose_name="Идентификатор начальника",
        blank=True,
        null=True
    )
    # Количество подчиненных высшего ранга
    number_subordinates_hr = models.IntegerField(
        verbose_name="Количество подчиненных высшего ранга",
        default=0
    )

    def __str__(self):
        """
        Если к объекту обращаются в виде строки, то возвращается id-начальства.
        Если возвращается Null - значит это самый верхний уровень
        """
        return self.name
