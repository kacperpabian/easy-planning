from django.contrib.auth.models import User
from django import forms


class UserFormRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')

    class Meta:
        labels = {'username': 'Login',
                  'email': 'Email'}
        error_messages = {
            'username': {
                'unique': 'Użytkownik z tym loginem już istnieje.'
            }
        }
        model = User
        fields = ['username', 'email', 'password']


class UserFormLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
