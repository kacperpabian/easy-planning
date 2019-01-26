# Generated by Django 2.1.3 on 2019-01-26 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('short_name', models.CharField(max_length=45)),
                ('is_selected', models.BooleanField(default=False)),
                ('school', models.ForeignKey(db_column='school_ID', on_delete=django.db.models.deletion.CASCADE, to='schools.School')),
            ],
            options={
                'db_table': 'class',
            },
        ),
    ]
