# Generated by Django 3.0.3 on 2020-03-15 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0004_person_chief'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='parent_id',
            new_name='parent',
        ),
    ]