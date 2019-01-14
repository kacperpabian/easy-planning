from django import forms

from .models import Subject


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        labels = {
            'name': 'Nazwa przedmiotu',
            'short_name': 'Skrócona nazwa'
        }
        fields = ['name', 'short_name']
