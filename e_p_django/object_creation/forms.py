from django.contrib.auth.models import User
# noinspection PyUnresolvedReferences
from start_page.models import (
    Schedule,
    SchoolBreakes,
    School
)
from django import forms


class SchoolForm(forms.ModelForm):

    class Meta:
        labels = {
            'cycle': 'Cykl',
            'school_year': 'Rok szkolny',
            'school_name': 'Nazwa szkoły',
            'description': 'Opis',
            'weekend_days': 'Dni weekendu',
            'start_time': 'Godzina rozpoczęcia zajęć',
            'max_lessons': 'Maksymalna liczba zajęć w ciągu dnia'
        }
        model = School
        fields = ['school_year', 'school_name', 'cycle',
                  'weekend_days', 'start_time', 'max_lessons', 'description']


class ScheduleForm(forms.ModelForm):

    class Meta:
        labels = {
            'name': 'Nazwa planu',
            'description': 'Opis'
        }
        model = Schedule
        fields = ['name', 'description']


class SchoolBreakesForm(forms.ModelForm):

    class Meta:
        model = SchoolBreakes
        labels = {
            'lesson_number': 'Numer zajęć',
            'break_time': 'Czas przerwy (minuty)'
        }
        fields = ['lesson_number', 'break_time']
