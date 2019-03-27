# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class School(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    description = models.CharField(max_length=60, blank=True, null=True)
    weekend_days = models.CharField(max_length=45)
    start_time = models.CharField(max_length=20)
    max_lessons = models.IntegerField()
    cycle = models.IntegerField()

    def get_absolute_url(self):
        return reverse('start_page:schools')

    class Meta:
        managed = True
        db_table = 'school'


class SchoolBreakes(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Field name made lowercase.
    lesson_number = models.IntegerField()
    break_time = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'school_breakes'
