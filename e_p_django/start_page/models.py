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
    email = models.CharField(unique=True, max_length=254)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class Class(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, db_column='schedule_ID')  # Field name made lowercase.
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
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')  # Field renamed because it was a Python reserved word.
    tutor = models.IntegerField()

    class Meta:
        db_table = 'class_teacher'


class Group(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'group'


class Lesson(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')  # Field renamed because it was a Python reserved word.
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, db_column='subject_ID')  # Field name made lowercase.
    room = models.ForeignKey('Room', on_delete=models.CASCADE, db_column='room_ID')  # Field name made lowercase.
    lesson_number = models.IntegerField()

    class Meta:
        db_table = 'lesson'


class Room(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, db_column='schedule_ID')  # Field name made lowercase.
    room_number = models.CharField(unique=True, max_length=10)
    capacity = models.IntegerField()

    class Meta:
        db_table = 'room'


class Schedule(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    cycle = models.IntegerField()
    school_year = models.CharField(max_length=45)
    school_name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, blank=True, null=True)
    weekend_days = models.CharField(max_length=45)
    start_time = models.CharField(max_length=45)
    max_lessons = models.CharField(max_length=45)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('start_page:schedules')

    def __str__(self):
        return self.school_year + ": " + self.name

    class Meta:
        db_table = 'schedule'


class SchoolBreakes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lesson_number = models.IntegerField()
    break_time = models.IntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, db_column='schedule_ID')  # Field name made lowercase.

    class Meta:
        db_table = 'school_breakes'


class Subject(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, db_column='schedule_ID')  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=45)
    short_name = models.CharField(max_length=45, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('start_page:object_creation:subjects', kwargs={'pk': self.schedule_id})

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'


class Teacher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, db_column='schedule_ID')  # Field name made lowercase.
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)

    class Meta:
        db_table = 'teacher'


class TeacherLesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'teacher_lesson'


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='teacher_ID')  # Field name made lowercase.
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, db_column='subject_ID')  # Field name made lowercase.

    class Meta:
        db_table = 'teacher_subject'
