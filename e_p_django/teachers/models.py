from django.db import models
from django.urls import reverse

from schools.models import School


class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)

    def get_absolute_url(self):
        return reverse('start_page:schools:teachers:teachers', kwargs={'pk': self.school_id})

    class Meta:
        managed = True
        db_table = 'teacher'
