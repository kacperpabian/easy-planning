from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        labels = {
            'name': 'Imię',
            'surname': 'Nazwisko'
        }
        fields = ['name', 'surname']
