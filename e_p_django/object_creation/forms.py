from django.contrib.auth.models import User
# noinspection PyUnresolvedReferences
from start_page.models import Schedule
from django import forms


class ScheduleForm(forms.ModelForm):

    class Meta:
        labels = {'name': 'Nazwa planu',
                  'cycle': 'Cykl',
                  'school_year': 'Rok planu',
                  'school_name': 'Nazwa szkoły',
                  'description': 'Opis',
                  'weekend_days': 'Dni weekendu',
                  'start_time': 'Godzina rozpoczęcia zajęć',
                  'max_lessons': 'Maksymalna liczba zajęć w ciągu dnia'}
        model = Schedule
        fields = ['name', 'school_year', 'school_name', 'cycle',
                  'weekend_days', 'start_time', 'max_lessons', 'description']
