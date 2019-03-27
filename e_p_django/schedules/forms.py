from django import forms

from .models import Schedule


class ScheduleForm(forms.ModelForm):

    class Meta:
        labels = {
            'name': 'Nazwa planu',
            'year': 'Rok rozpoczęcia',
            'description': 'Opis',
            'class_field': 'Klasa'
        }
        model = Schedule
        fields = ['name', 'year', 'description', 'class_field']
