from django.db import models
from django.urls import reverse

from schools.models import School


class Subject(models.Model):
    name = models.CharField(unique=True, max_length=45)
    short_name = models.CharField(max_length=45)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('start_page:schools:subjects:subjects', kwargs={'pk': self.school_id})

    class Meta:
        managed = True
        db_table = 'subject'
