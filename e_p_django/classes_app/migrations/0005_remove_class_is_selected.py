# Generated by Django 2.2.1 on 2019-05-25 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes_app', '0004_auto_20190324_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='is_selected',
        ),
    ]
