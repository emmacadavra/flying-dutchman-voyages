from django import forms


class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('CAP', 'CAPTAINS QUARTERS'),
        ('OCD', 'DOUBLE CABIN'),
        ('OCS', 'SINGLE CABIN'),
        ('CRW', 'CREW BUNKS'),
    )
    
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    booking_date = forms.DateField(required=True)
    num_passengers = forms.IntegerField()
