from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
from .models import Room, Booking
from .forms import AvailabilityForm
from fd_bookings.booking_functions.availability import check_availability


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
        rooms = Room.object.filter(category=data['room_category'])
        available_rooms = []

        for room in rooms:
            if check_availability(room, data['booking_date']):
                available_rooms.append(room)

        if len(available_rooms)>0:

            room = available_rooms[0]
            booking = Booking.objects.create(
                user = request.user,
                room = room,
                booking_date = data['booking_date'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This room type is not available.')