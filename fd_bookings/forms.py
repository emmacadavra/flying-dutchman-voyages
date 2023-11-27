import datetime
from django import forms
from .models import Room
from django.core.exceptions import ValidationError


class BookingForm(forms.Form):
    ROOM_CATEGORIES = (
        ('CAPQ', 'Captain\'s Quarters'),
        ('DCBN', 'Double Cabin'),
        ('SCBN', 'Single Cabin'),
        ('CRWH', 'Crew Hammocks'),
    )

    room_id = None
    booking_date = forms.DateField(label='Date of Departure:', required=True)
    num_passengers = forms.IntegerField(label='Number of Passengers:', required=True)

    def __init__(self, *args, **kwargs):
        self.room_id = kwargs.pop('room_id')
        super(BookingForm, self).__init__(*args, **kwargs)

    def clean(self):
        room = Room.objects.get(id=self.room_id)
        today = datetime.date.today()

        if 'num_passengers' in self.cleaned_data and self.cleaned_data['num_passengers'] > room.capacity:
            raise ValidationError(
                'Number of passengers exceeds maximum room capacity.'
            )

        if 'booking_date' in self.cleaned_data and self.cleaned_data['booking_date'] <= today:
            raise ValidationError(
                'Your selected date of departure must not be in the past.'
            )

        if 'booking_date' in self.cleaned_data and self.cleaned_data['booking_date'].weekday() != 6:
            raise ValidationError(
                'The Flying Dutchman only sets sail on Sundays!'
            )
