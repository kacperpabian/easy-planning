from django.db import models
from django.urls import reverse

from schools.models import School
from classes_app.models import Class


class ScheduleDate(models.Model):
    year = models.PositiveSmallIntegerField(default=None)

    def __str__(self):
        return str(self.year)

    class Meta:
        managed = True
        db_table = 'schedule_date'


class Schedule(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Field name made lowercase.
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column="class_id")  # Field name made lowercase.
    year = models.ForeignKey(ScheduleDate, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('start_page:schools')

    def __str__(self):
        return str(self.year.year) + " (" + self.name + ")"

    class Meta:
        managed = True
        db_table = 'schedule'
