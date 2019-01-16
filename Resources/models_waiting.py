class ClassGroup(models.Model):
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'class_group'


class ClassTeacher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')  # Field renamed because it was a Python reserved word.
    tutor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class_teacher'


class Lesson(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')  # Field renamed because it was a Python reserved word.
    group = models.ForeignKey(Group, models.DO_NOTHING)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, db_column='subject_ID')  # Field name made lowercase.
    room = models.ForeignKey('Room', models.DO_NOTHING, db_column='room_ID')  # Field name made lowercase.
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, db_column='schedule_ID')  # Field name made lowercase.
    lesson_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lesson'


class TeacherLesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'teacher_lesson'

class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='teacher_ID')  # Field name made lowercase.
    subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column='subject_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacher_subject'


class Group(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group'
