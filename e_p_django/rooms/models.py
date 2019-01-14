from django.db import models
from django.urls import reverse

from start_page.models import School


class Room(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_ID')  # Field name made lowercase.
    room_number = models.CharField(unique=True, max_length=10)
    capacity = models.IntegerField()

    def get_absolute_url(self):
        return reverse('start_page:object_creation:rooms:rooms', kwargs={'pk': self.school_id})

    class Meta:
        managed = False
        db_table = 'room'
