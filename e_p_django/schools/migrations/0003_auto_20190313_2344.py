# Generated by Django 2.1.5 on 2019-03-13 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_auto_20190313_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
