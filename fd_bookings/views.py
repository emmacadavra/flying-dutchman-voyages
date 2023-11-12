from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
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


class RoomList(generic.ListView):
    model = Room
    template_name = 'room_list.html'


class BookingList(generic.ListView):
    model = Booking
    template_name = 'booking_list.html'




# tutorial code
# class RoomDetailView(View):
#     def get(self, request, *args, **kwargs):
#         room_category = self.kwargs.get('category', None)
#         rooms = Room.object.filter(category=room_category)
#         room = room_category[0]
#         context = {
#             'room_category': room.category
#         }
#         return render(request, 'room_detail.html', context)
        

#     def post(self, request, *args, **kwargs):
#         rooms = Room.object.filter(category=category)
#         available_rooms = []

#         for room in rooms:
#             if check_availability(room, data['booking_date']):
#                 available_rooms.append(room)

#         if len(available_rooms)>0:
#             room = available_rooms[0]
#             booking = Booking.objects.create(
#                 user = self.request.user,
#                 room = room,
#                 booking_date = data['booking_date'],
#             )
#             booking.save()
#             return HttpResponse(booking)
#         else:
#             return HttpResponse('This room type is not available.')

# class BookingView(generic.FormView):
#     form_class = AvailabilityForm
#     template_name = 'fd_bookings/make_booking.html'

#     def valid_form(self, form):
#         data = form.cleaned_data
#         rooms = Room.object.filter(category=data['room_category'])
#         available_rooms = []

#         for room in rooms:
#             if check_availability(room, data['booking_date']):
#                 available_rooms.append(room)

#         if len(available_rooms)>0:

#             room = available_rooms[0]
#             booking = Booking.objects.create(
#                 user = self.request.user,
#                 room = room,
#                 booking_date = data['booking_date'],
#             )
#             booking.save()
#             return HttpResponse(booking)
#         else:
#             return HttpResponse('This room type is not available.')