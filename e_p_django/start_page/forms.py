from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
from . import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



