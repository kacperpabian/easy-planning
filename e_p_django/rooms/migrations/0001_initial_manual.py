# Generated by Django 2.1.5 on 2019-03-13 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial_migrate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=10, unique=True)),
                ('capacity', models.IntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.School')),
            ],
            options={
                'db_table': 'room',
                'managed': True,
            },
        ),
    ]
