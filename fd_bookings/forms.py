import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Room
from fd_bookings.booking_functions.check_availability import check_availability


class DateInput(forms.DateInput):
    """
    A widget that replaces Django's default text field for date input
    with a date picker which is easier for users to use.
    """
    input_type = 'date'


class BookingForm(forms.Form):
    """
    The main form for creating and amending bookings.
    """
    room_id = None
    user_id = None
    booking_date = forms.DateField(widget=DateInput, label='Date of Departure:', required=True)
    num_passengers = forms.IntegerField(label='Number of Passengers:', required=True)

    def __init__(self, *args, **kwargs):
        """
        A custom addition to the form's __init__ function, due to additional
        rules being added to the default clean function
        """
        self.room_id = kwargs.pop('room_id')
        self.user_id = kwargs.pop('user_id') if 'user_id' in kwargs else None
        super(BookingForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        Additional rules added to Django Forms' clean function that check
        the data entered into the form and validate it.
        """
        room = Room.objects.get(id=self.room_id)
        today = datetime.date.today()

        if 'num_passengers' in self.cleaned_data and self.cleaned_data['num_passengers'] > room.capacity:
            raise ValidationError(
                f'Number of passengers exceeds maximum room capacity {room.capacity}.'
            )

        if 'num_passengers' in self.cleaned_data and self.cleaned_data['num_passengers'] <= 0:
            raise ValidationError(
                'Number of passengers must be greater than 0.'
            )

        if 'booking_date' in self.cleaned_data and self.cleaned_data['booking_date'] <= today:
            raise ValidationError(
                'Your selected date of departure must not be in the past.'
            )

        if 'booking_date' in self.cleaned_data and self.cleaned_data['booking_date'].weekday() != 6:
            raise ValidationError(
                'The Flying Dutchman only sets sail on Sundays!'
            )

        if 'booking_date' in self.cleaned_data and check_availability(self.room_id, self.cleaned_data['booking_date'], self.user_id) is not True:
            raise ValidationError(
                "This room is not available for this departure date."
            )
