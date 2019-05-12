from django.db import models

from classes_app.models import Class
from schedules.models import Schedule
from rooms.models import Room
from subjects.models import Subject
from teachers.models import Teacher


class Group(models.Model):

    class Meta:
        managed = True
        db_table = 'group'


class Lesson(models.Model):
    days_choices = (('1', 'Pon'), ('2', 'Wt'), ('3', 'Śr'), ('4', 'Czw'), ('5', 'Pt'), ('6', 'Sob'), ('7', 'Nie'))
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)  # Field renamed because it was a Python reserved word.
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=None, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Field name made lowercase.
    room = models.ForeignKey(Room, models.DO_NOTHING)  # Field name made lowercase.
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)  # Field name made lowercase.
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    lesson_number = models.IntegerField()
    day = models.CharField(default=None, max_length=20, choices=days_choices)

    class Meta:
        managed = True
        db_table = 'lesson'
