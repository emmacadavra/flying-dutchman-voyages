from django.shortcuts import render
from django.views import generic, View
from .models import Room, Booking


# Create your views here.
class RoomList(generic.ListView):
    model = Room
    template_name = "index.html"


class BookingList(generic.ListView):
    model = Booking
    template_name = "bookings.html"
