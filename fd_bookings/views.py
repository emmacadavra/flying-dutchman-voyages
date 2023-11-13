from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Room, Booking
from .forms import AvailabilityForm
from fd_bookings.booking_functions.availability import check_availability


# Create your views here.
def home(request):
    return render(request, 'index.html',)


def events(request):
    return render(request, 'events.html',)


def contact(request):
    return render(request, 'contact.html',)


def RoomList(request):
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)
    room_values = room_categories.values()
    room_list = []

    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('fd_bookings:RoomDetailView', kwargs={'category': room_category})
        
        room_list.append((room, room_url))

    context = {
        "room_list": room_list,
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


# tutorial code
class RoomDetailView(generic.View):
    def get(self, request, *args, **kwargs):
        room_category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=room_category)

        if len(room_list)>0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)
            context = {
                'room_category': room_category,
                'form': form,
            }
            return render(request, 'fd_bookings/room_detail.html', context)
        else:
            return HttpResponse('Room category does not exist.')

    def post(self, request, *args, **kwargs):
        room_category = self.kwargs.get('category', None)
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
            return HttpResponse(booking)
        else:
            return HttpResponse('This room is not available.')


#tutorial code
# class BookingView(generic.FormView):
#     form_class = AvailabilityForm
#     template_name = 'fd_bookings/room_detail.html'

#     def form_valid(self, form):

#         data = form.cleaned_data
#         room_list = Room.objects.filter(category=data['room_category'])
#         available_rooms = []

#         for room in room_list:
#             if check_availability(room, data['booking_date']):
#                 available_rooms.append(room)

#         if form.is_valid():
#             if len(available_rooms)>0:
#                 room = available_rooms[0]
#                 booking = Booking.objects.create(
#                     user = self.request.user,
#                     room = room,
#                     booking_date = data['booking_date'],
#                     num_passengers = data['num_passengers']
#                 )
#                 booking.save()
#                 return HttpResponse(booking)
#             else:
#                 return HttpResponse('Unavailable - please try a different room.')

class CancelBooking(generic.DeleteView):
    model = Booking
    success_url = reverse_lazy('fd_bookings:ViewBookingList')
