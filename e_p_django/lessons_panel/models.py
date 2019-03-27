from django.db import models

from classes_app.models import Class
from schedules.models import Schedule
from rooms.models import Room
from subjects.models import Subject


class Group(models.Model):

    class Meta:
        managed = True
        db_table = 'group'


class Lesson(models.Model):
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)  # Field renamed because it was a Python reserved word.
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=None, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Field name made lowercase.
    room = models.ForeignKey(Room, models.DO_NOTHING)  # Field name made lowercase.
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)  # Field name made lowercase.
    lesson_number = models.IntegerField()
    test = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'lesson'
