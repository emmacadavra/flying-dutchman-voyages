from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Room, Booking
from .forms import AvailabilityForm
from fd_bookings.booking_functions.check_availability import check_availability
from fd_bookings.booking_functions.get_room_category_urls import get_room_category_urls
from fd_bookings.booking_functions.get_category_string import get_category_string


def home_page(request):
    return render(request, 'index.html',)


def events_page(request):
    return render(request, 'events.html',)


def contact_page(request):
    return render(request, 'contact.html',)


def RoomList(request):
    room_category_urls = get_room_category_urls()

    context = {
        "room_list": room_category_urls,
    }
    return(render(request, 'fd_bookings/our_rooms.html', context))


class ViewBookingList(generic.ListView):
    model = Booking
    template_name = 'fd_bookings/manage_bookings.html'
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list
        

class RoomDetailView(generic.View):
    def get(self, request, *args, **kwargs):
        room_category = kwargs.get('category', None)
        category_string = get_category_string(room_category)
        form = AvailabilityForm()

        if category_string is not None:
        #  NEED TO INVESTIGATE HOW TO DISPLAY BEDS + CAPACITY AS IT IS NOT CURRENTLY WORKING
            context = {
                'room_category': category_string,
                'form': form,
            }
            return render(request, 'fd_bookings/room_detail.html', context)
        else:
    # NEED TO UPDATE THIS TO BETTER RESPONSES/REDIRECTS
            return HttpResponse('Room category does not exist.')


    def post(self, request, *args, **kwargs):
        room_category = kwargs.get('category', None)
        room_list = Room.objects.filter(category=room_category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []

        for room in room_list:
            if check_availability(room, data['booking_date']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                booking_date = data['booking_date'],
                num_passengers = data['num_passengers']
            )
            booking.save()

# NEED TO UPDATE THESE TO BETTER RESPONSES/REDIRECTS
            return HttpResponse(booking)
        else:
            return HttpResponse('This room is not available.')


class CancelBooking(generic.DeleteView):
    model = Booking
    template_name = 'fd_bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('fd_bookings:ViewBookingList')
