from django import forms

from .models import Lesson
from schedules.models import Schedule
from classes_app.models import Class


class LessonForm(forms.ModelForm):
    class Meta:
        labels = {
            'group': 'Grupa',
            'subject': 'Przedmiot',
            'room': 'Pokój',
            'lesson_number': 'Numer lekcji'
        }
        model = Lesson
        fields = ['group', 'subject', 'room', 'lesson_number']


class ScheduleCombo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        school_pk = kwargs.pop('school_pk', None)
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if school_pk is not None:
            schedules = Schedule.objects.filter(school_id=school_pk)
            self.fields['class_field'].queryset = Class.objects.filter(school_id=school_pk)
            self.fields['schedule'].queryset = schedules.exclude(
                year=None).values_list('year', flat=True).distinct()


    class Meta:
        labels = {
            'class_field': 'Klasa',
            'schedule': 'Rok'
        }
        model = Lesson
        fields = ['schedule', 'class_field']

# class ScheduleCombo(forms.Form):
#     schedules = None
#
#     def __init__(self, *args, **kwargs):
#         self.school_id = kwargs.pop('school_id')
#         super(ScheduleCombo, self).__init__(*args, **kwargs)
#         self.schedules = Schedule.objects.all().filter(school_id=self.school_id)
#
#     forms.ModelChoiceField(queryset=schedules)
