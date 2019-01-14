# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Group(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group'


class School(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, db_column='user_id')
    school_year = models.CharField(max_length=20)
    school_name = models.CharField(max_length=100)
    description = models.CharField(max_length=60, blank=True, null=True)
    weekend_days = models.CharField(max_length=45)
    start_time = models.CharField(max_length=20)
    max_lessons = models.IntegerField()
    cycle = models.IntegerField()

    def get_absolute_url(self):
        return reverse('start_page:schools')

    class Meta:
        managed = False
        db_table = 'school'


class Schedule(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_ID')  # Field name made lowercase.
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('start_page:schools')

    class Meta:
        managed = False
        db_table = 'schedule'


class SchoolBreakes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_ID')  # Field name made lowercase.
    lesson_number = models.IntegerField()
    break_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'school_breakes'
