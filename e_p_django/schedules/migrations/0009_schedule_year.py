# Generated by Django 2.1.7 on 2019-03-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0008_remove_schedule_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
