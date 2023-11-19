from django import forms
from django.core.exceptions import ValidationError


class AvailabilityForm(forms.Form):
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

