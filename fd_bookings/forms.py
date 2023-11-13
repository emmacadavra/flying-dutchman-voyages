from django import forms


class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('CAP', 'CAPTAIN\'S QUARTERS'),
        ('OCD', 'DOUBLE CABIN'),
        ('OCS', 'SINGLE CABIN'),
        ('CRW', 'CREW BUNKS'),
    )
    
    booking_date = forms.DateField(required=True)
    num_passengers = forms.IntegerField(required=True)
