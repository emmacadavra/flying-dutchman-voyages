from django import forms


class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('CAPQ', 'Captain\'s Quarters'),
        ('DCBN', 'Double Cabin'),
        ('SCBN', 'Single Cabin'),
        ('CRWH', 'Crew Hammocks'),
    )
    
    booking_date = forms.DateField(required=True)
    num_passengers = forms.IntegerField(required=True)
