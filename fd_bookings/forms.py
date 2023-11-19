from django import forms


class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('CAPQ', 'CAPTAIN\'S QUARTERS'),
        ('DCBN', 'DOUBLE CABIN'),
        ('SCBN', 'SINGLE CABIN'),
        ('CRWH', 'CREW BUNKS'),
    )
    
    booking_date = forms.DateField(required=True)
    num_passengers = forms.IntegerField(required=True)
