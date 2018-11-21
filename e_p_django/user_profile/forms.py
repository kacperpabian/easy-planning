from django.contrib.auth.models import User
from django import forms


class UserFormProfile(forms.ModelForm):

    class Meta:
        labels = {'username': 'Login',
                  'email': 'Email',
                  'first_name': 'Imię',
                  'last_name': 'Nazwisko'}
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserChangePassword(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Stare hasło:')

    class Meta:
        model = User
        fields = ['password']
