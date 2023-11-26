from django import forms
from .models import Room, Booking
from django.core.exceptions import ValidationError


class BookingForm(forms.Form):
    ROOM_CATEGORIES = (
        ('CAPQ', 'Captain\'s Quarters'),
        ('DCBN', 'Double Cabin'),
        ('SCBN', 'Single Cabin'),
        ('CRWH', 'Crew Hammocks'),
    )

    room_id = None
    booking_date = forms.DateField(required=True)
    num_passengers = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        self.room_id = kwargs.pop('room_id')
        super(BookingForm, self).__init__(*args, **kwargs)

    def clean(self):
        room = Room.objects.get(id=self.room_id)

        if self.cleaned_data['num_passengers'] > room.capacity:
            raise ValidationError(
                "Number of passengers exceeds maximum capacity."
            )