from django import forms

from .models import Class


class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        labels = {
            'name': 'Nazwa',
            'short_name': 'Skrócona nazwa'
        }
        fields = ['name', 'short_name']
