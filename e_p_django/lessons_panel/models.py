from django.db import models

from classes_app.models import Class
from schedules.models import Schedule
from rooms.models import Room
from subjects.models import Subject


class Group(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group'


class Lesson(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')  # Field renamed because it was a Python reserved word.
    group = models.ForeignKey(Group, models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, db_column='subject_ID')  # Field name made lowercase.
    room = models.ForeignKey(Room, models.DO_NOTHING, db_column='room_ID')  # Field name made lowercase.
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, db_column='schedule_ID')  # Field name made lowercase.
    lesson_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lesson'