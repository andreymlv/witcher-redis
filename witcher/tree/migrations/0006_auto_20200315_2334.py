# Generated by Django 3.0.3 on 2020-03-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0005_auto_20200315_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='identifier',
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор'),
        ),
    ]