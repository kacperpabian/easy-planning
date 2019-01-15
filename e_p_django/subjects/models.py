from django.db import models
from django.urls import reverse

from school_schedule.models import School


class Subject(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=45)
    short_name = models.CharField(max_length=45)
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_ID')  # Field name made lowercase.

    def get_absolute_url(self):
        return reverse('start_page:school_schedule:subjects:subjects', kwargs={'pk': self.school_id})

    class Meta:
        managed = False
        db_table = 'subject'
