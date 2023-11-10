from django.shortcuts import render
from django.views import generic, View
from .models import Room, Booking
from .forms import AvailabilityForm
from booking_functions.availability import check_availability


# Create your views here.
class RoomList(generic.ListView):
    model = Room
    template_name = 'index.html'


# class BookingList(generic.ListView):
#     model = Booking
#     template_name = 'bookings.html'

class BookingView(generic.FormView):
    form_class = AvailabilityForm
    template_name = 'bookings.html'

    def valid_form(self, form):
        data = form.cleaned_data

