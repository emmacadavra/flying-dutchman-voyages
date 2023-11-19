from django import forms


class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('CAPQ', 'Captain\'s Quarters'),
        ('DCBN', 'Double Cabin'),
        ('SCBN', 'Single Cabin'),
        ('CRWH', 'Crew Hammocks'),
    )

    # def validate_sunday(value):
    #     if value is not 6:
    #         raise ValidationError(
    #             ('%(value)s is not a valid day of departure'), params={'value': value},
    #         )
    # booking_date = forms.DateField(validators=[validate_sunday])
    booking_date = forms.DateField(required=True)
    num_passengers = forms.IntegerField(required=True)

