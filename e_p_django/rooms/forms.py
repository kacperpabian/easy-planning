from django import forms

from .models import Room


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        labels = {
            'room_number': 'Numer pokoju',
            'capacity': 'Liczba miejsc'
        }
        fields = ['room_number', 'capacity']
