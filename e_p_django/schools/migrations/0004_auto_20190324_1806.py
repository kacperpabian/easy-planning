# Generated by Django 2.1.5 on 2019-03-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20190313_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='schoolbreakes',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
