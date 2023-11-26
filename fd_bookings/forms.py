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

    # def validate_sunday(value):
    #     if value != 6:
    #         raise ValidationError(
    #             ('%(value)s is not a valid day of departure'), params={'value': value},
    #         )

    # booking_date = forms.DateField(validators=[validate_sunday], required=True)
    booking_date = forms.DateField(required=True)
    num_passengers = forms.IntegerField(required=True)


    def clean(self):
        booking = Booking.objects.get(id=1)
        if self.cleaned_data['num_passengers'] > booking.room.capacity:
            raise ValidationError(
                "Number of passengers exceeds maximum capacity."
            )
