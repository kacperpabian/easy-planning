from django.db import models
from django.urls import reverse

from e_p_django.classes_app.models import Class
from e_p_django.schedules.models import Schedule
from e_p_django.rooms.models import Room
from e_p_django.subjects.models import Subject
from e_p_django.teachers.models import Teacher


class Group(models.Model):

    class Meta:
        managed = True
        db_table = 'group'


class Lesson(models.Model):
    days_choices = (('1', 'Pon'), ('2', 'Wt'), ('3', 'Śr'), ('4', 'Czw'), ('5', 'Pt'), ('6', 'Sob'), ('7', 'Nie'))
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=None, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Field name made lowercase.
    room = models.ForeignKey(Room, models.DO_NOTHING)  # Field name made lowercase.
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)  # Field name made lowercase.
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    lesson_number = models.IntegerField()
    day = models.CharField(default=None, max_length=20, choices=days_choices)

    def get_absolute_url(self):
        return reverse('start_page:schools:lessons_panel:lessons-panel', kwargs={'pk': self.schedule.school_id})

    class Meta:
        managed = True
        db_table = 'lesson'
