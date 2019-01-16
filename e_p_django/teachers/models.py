from django.db import models
from django.urls import reverse

from schools.models import School


class Teacher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_ID')  # Field name made lowercase.
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)

    def get_absolute_url(self):
        return reverse('start_page:schools:teachers:teachers', kwargs={'pk': self.school_id})

    class Meta:
        managed = False
        db_table = 'teacher'
