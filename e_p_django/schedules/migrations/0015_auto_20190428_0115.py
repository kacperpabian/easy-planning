# Generated by Django 2.1.7 on 2019-04-27 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0014_auto_20190428_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.ScheduleDate'),
        ),
    ]
