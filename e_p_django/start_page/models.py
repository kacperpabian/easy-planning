# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Breakes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    days_definition = models.ForeignKey('DaysDefinition', models.CASCADE, db_column='Days_definition_ID')  # Field name made lowercase.
    lesson_number = models.IntegerField(db_column='Lesson_number')  # Field name made lowercase.
    break_time = models.IntegerField(db_column='Break_time')  # Field name made lowercase.

    class Meta:
        db_table = 'breakes'


class Class(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey('School', models.DO_NOTHING, db_column='School_ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    short_name = models.CharField(db_column='Short_name', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'class'


class ClassGroup(models.Model):
    class_field = models.ForeignKey(Class, models.CASCADE, db_column='Class_ID')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    group = models.ForeignKey('Group', models.CASCADE, db_column='Group_ID')  # Field name made lowercase.

    class Meta:
        db_table = 'Class_Group'


class ClassTeacher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey('Teacher', models.CASCADE, db_column='Teacher_ID')  # Field name made lowercase.
    class_field = models.ForeignKey(Class, models.CASCADE, db_column='Class_ID')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    tutor = models.IntegerField(db_column='Tutor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'class_teacher'


class DaysDefinition(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey('Schedule', models.CASCADE, db_column='Schedule_ID')  # Field name made lowercase.
    weekend_days = models.CharField(db_column='Weekend_days', max_length=45)  # Field name made lowercase.
    start_time = models.CharField(db_column='Start_time', max_length=45)  # Field name made lowercase.
    max_lessons = models.CharField(db_column='Max_lessons', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'days_definition'


class Group(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'group'


class Lesson(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    class_field = models.ForeignKey(Class, models.CASCADE, db_column='Class_ID')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    group = models.ForeignKey(Group, models.CASCADE, db_column='Group_ID')  # Field name made lowercase.
    lesson_number = models.IntegerField(db_column='Lesson_number')  # Field name made lowercase.

    class Meta:
        db_table = 'lesson'


class Room(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey('School', models.CASCADE, db_column='School_ID')  # Field name made lowercase.
    lesson = models.ForeignKey(Lesson, models.CASCADE, db_column='Lesson_ID')  # Field name made lowercase.
    room_number = models.CharField(db_column='Room_number', unique=True, max_length=10)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity')  # Field name made lowercase.

    class Meta:
        db_table = 'room'


class Schedule(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.CASCADE, db_column='User_ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    cycle = models.IntegerField(db_column='Cycle')  # Field name made lowercase.
    school_year = models.CharField(db_column='School_year', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'schedule'


class School(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey(Schedule, models.CASCADE, db_column='Schedule_ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'school'


class Subject(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey('Teacher', models.CASCADE, db_column='Teacher_ID')  # Field name made lowercase.
    school = models.ForeignKey(School, models.CASCADE, db_column='School_ID')  # Field name made lowercase.
    lesson = models.ForeignKey(Lesson, models.CASCADE, db_column='Lesson_ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=45)  # Field name made lowercase.
    short_name = models.CharField(db_column='Short_name', unique=True, max_length=3)  # Field name made lowercase.

    class Meta:
        db_table = 'subject'


class Teacher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'teacher'


class TeacherLesson(models.Model):
    teacher = models.ForeignKey(Teacher, models.CASCADE, db_column='Teacher_ID')  # Field name made lowercase.
    lesson = models.ForeignKey(Lesson, models.CASCADE, db_column='Lesson_ID')  # Field name made lowercase.

    class Meta:
        db_table = 'teacher_lesson'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'user'
