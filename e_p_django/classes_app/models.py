from django.db import models
from django.urls import reverse

from schools.models import School


class Class(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_ID')  # Field name made lowercase.
    name = models.CharField(max_length=45)
    short_name = models.CharField(max_length=45)

    def get_absolute_url(self):
        return reverse('start_page:schools:classes_app:classes', kwargs={'pk': self.school_id})

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'class'
