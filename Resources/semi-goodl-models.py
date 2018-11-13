# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
        db_table = 'auth_user'


class Class(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    short_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'class'


class ClassGroup(models.Model):
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')  # Field renamed because it was a Python reserved word.
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    class Meta:
        db_table = 'class_group'


class ClassTeacher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    tutor = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'class_teacher'


class DaysDefinition(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    weekend_days = models.CharField(max_length=45)
    start_time = models.CharField(max_length=45)
    max_lessons = models.CharField(max_length=45)

    class Meta:
        db_table = 'days_definition'


class Group(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'group'


class Schedule(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, db_column='user_id')
    name = models.CharField(max_length=45)
    cycle = models.IntegerField()
    school_year = models.CharField(max_length=45)

    def __str__(self):
        return self.school_year + " - " + self.name

    class Meta:
        db_table = 'schedule'


class School(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'school'


class Subject(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=45)
    short_name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'


class Lesson(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')  # Field renamed because it was a Python reserved word.
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, db_column='subject_id')
    group = models.ForeignKey(Group, models.DO_NOTHING)
    lesson_number = models.IntegerField()

    class Meta:
        db_table = 'lesson'


class Room(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    room_number = models.CharField(unique=True, max_length=10)
    capacity = models.IntegerField()

    class Meta:
        db_table = 'room'


class SchoolBreakes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    days_definition = models.ForeignKey(DaysDefinition, on_delete=models.CASCADE)
    lesson_number = models.IntegerField()
    break_time = models.IntegerField()

    class Meta:
        db_table = 'school_breakes'


class Teacher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)

    class Meta:
        db_table = 'teacher'


class TeacherLesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'teacher_lesson'
