from django.db import models
from django.urls import reverse

from schools.models import School
from classes_app.models import Class


class Schedule(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_id')  # Field name made lowercase.
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')  # Field name made lowercase.
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('start_page:schools')

    class Meta:
        managed = True
        db_table = 'schedule'
