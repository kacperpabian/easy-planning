from django import forms

from .models import Schedule


class ScheduleForm(forms.ModelForm):

    class Meta:
        labels = {
            'name': 'Nazwa planu',
            'description': 'Opis',
            'class_field': 'Klasa'
        }
        model = Schedule
        fields = ['name', 'description', 'class_field']
