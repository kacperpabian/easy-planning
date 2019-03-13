from django.db import models
from django.urls import reverse

from schools.models import School


class Room(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Field name made lowercase.
    room_number = models.CharField(unique=True, max_length=10)
    capacity = models.IntegerField()

    def __str__(self):
        return self.room_number

    def get_absolute_url(self):
        return reverse('start_page:schools:rooms:rooms', kwargs={'pk': self.school_id})

    class Meta:
        managed = True
        db_table = 'room'
