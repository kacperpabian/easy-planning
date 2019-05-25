from django import forms

from .models import Schedule, ScheduleDate
from classes_app.models import Class


class ScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        school_pk = kwargs.pop('school_pk', None)
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if school_pk is not None:
            self.fields['class_field'].queryset = Class.objects.filter(school_id=school_pk)

    class Meta:
        labels = {
            'name': 'Nazwa planu',
            'description': 'Opis',
            'class_field': 'Klasa'
        }
        model = Schedule
        fields = ['name', 'description', 'class_field', 'year']


class ScheduleDateForm(forms.ModelForm):
    class Meta:
        labels = {
            'year': 'Rok'
        }
        model = ScheduleDate
        fields = ['year']
