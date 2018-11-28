from django.contrib.auth.models import User
# noinspection PyUnresolvedReferences
from start_page.models import (
    Schedule,
    Subject,
    Room,
    Teacher
)
from django import forms


class ScheduleForm(forms.ModelForm):

    class Meta:
        labels = {
            'name': 'Nazwa planu',
            'cycle': 'Cykl',
            'school_year': 'Rok planu',
            'school_name': 'Nazwa szkoły',
            'description': 'Opis',
            'weekend_days': 'Dni weekendu',
            'start_time': 'Godzina rozpoczęcia zajęć',
            'max_lessons': 'Maksymalna liczba zajęć w ciągu dnia'
        }
        model = Schedule
        fields = ['name', 'school_year', 'school_name', 'cycle',
                  'weekend_days', 'start_time', 'max_lessons', 'description']


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        labels = {
            'name': 'Nazwa przedmiotu',
            'short_name': 'Skrócona nazwa'
        }
        fields = ['name', 'short_name']


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        labels = {
            'room_number': 'Numer pokoju',
            'capacity': 'Liczba miejsc'
        }
        fields = ['room_number', 'capacity']


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        labels = {
            'name': 'Imię',
            'surname': 'Nazwisko'
        }
        fields = ['name', 'surname']
