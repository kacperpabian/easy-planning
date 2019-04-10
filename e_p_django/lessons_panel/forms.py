from django import forms

from .models import Lesson
from schedules.models import Schedule


class LessonForm(forms.ModelForm):

    class Meta:
        labels = {
            'group': 'Grupa',
            'subject': 'Przedmiot',
            'room': 'Pokój',
            'lesson_number': 'Numer lekcji'
        }
        model = Lesson
        fields = ['group', 'subject', 'room', 'lesson_number', 'class_field']


class ScheduleCombo(forms.ModelForm):
    class Meta:
        labels = {
            'schedule': 'Rok'
        }
        model = Lesson
        fields = ['schedule']


# class ScheduleCombo(forms.Form):
#     schedules = None
#
#     def __init__(self, *args, **kwargs):
#         self.school_id = kwargs.pop('school_id')
#         super(ScheduleCombo, self).__init__(*args, **kwargs)
#         self.schedules = Schedule.objects.all().filter(school_id=self.school_id)
#
#     forms.ModelChoiceField(queryset=schedules)

