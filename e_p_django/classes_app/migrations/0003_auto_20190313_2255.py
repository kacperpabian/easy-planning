# Generated by Django 2.1.5 on 2019-03-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes_app', '0002_auto_20190313_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
