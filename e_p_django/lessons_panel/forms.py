from django import forms

from .models import Lesson
from schedules.models import ScheduleDate
from schedules.models import Schedule
from classes_app.models import Class
from schools.models import School
from django_select2.forms import ModelSelect2Widget


class LessonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        work_dict = kwargs.pop('work_dict', None)
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if work_dict:
            work_dict = ((str(key), value) for key, value in work_dict.items())
            if work_dict:
                self.fields['day'] = forms.ChoiceField(required=False, choices=work_dict, widget=forms.Select())

    class Meta:
        labels = {
            'group': 'Grupa',
            'subject': 'Przedmiot',
            'room': 'Pokój',
            'lesson_number': 'Numer lekcji',
            'day': 'Dzień'
        }
        model = Lesson
        fields = ['group', 'subject', 'room', 'lesson_number', 'day']


class ScheduleCombo(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        school_pk = kwargs.pop('school_pk', None)
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if school_pk is not None:
            school = School.objects.get(id=school_pk)
            self.fields['class_field'].queryset = school.class_set.all()
            self.fields['schedule'].queryset = school.schedule_set.none()

        if 'schedule' in self.data:
            try:
                class_id = int(self.data.get('class_field'))
                self.fields['schedule'].queryset = Schedule.objects.filter(class_field_id=class_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['schedule'].queryset = self.instance.class_field.schedule_set.order_by('name')

    class Meta:
        labels = {
            'class_field': 'Klasa',
            'schedule': 'Rok'
        }
        model = Lesson
        fields = ['class_field', 'schedule']

# class ScheduleCombo(forms.Form):
#     schedules = None
#
#     def __init__(self, *args, **kwargs):
#         self.school_id = kwargs.pop('school_id')
#         super(ScheduleCombo, self).__init__(*args, **kwargs)
#         self.schedules = Schedule.objects.all().filter(school_id=self.school_id)
#
#     forms.ModelChoiceField(queryset=schedules)
