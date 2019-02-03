from django import forms

from .models import Lesson


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
