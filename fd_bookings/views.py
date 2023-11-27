from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import Room, Booking
from .forms import BookingForm
from fd_bookings.booking_functions.check_availability import check_availability
from fd_bookings.booking_functions.get_room_category_urls import get_room_category_urls


def home_page(request):
    # ADD DOCSTRING
    return render(request, 'index.html',)


def events_page(request):
    # ADD DOCSTRING
    return render(request, 'events.html',)


def contact_page(request):
    # ADD DOCSTRING
    return render(request, 'contact.html',)


def room_list(request):
    # ADD DOCSTRING
    room_category_urls = get_room_category_urls()

    context = {
        "room_list": room_category_urls,
    }
    return render(request, 'fd_bookings/our_rooms.html', context)


class ViewBookingList(generic.ListView):
    # ADD DOCSTRING
    # paginate_by = 5 (https://docs.djangoproject.com/en/4.2/topics/pagination/ - follow instructions in template)
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
    # ADD DOCSTRINGS
    def get(self, request, *args, **kwargs):
        room_category = kwargs.get('category', None)
        room_list = Room.objects.filter(category=room_category)

        if len(room_list) > 0:  # Need to consider if this is necessary
            room = room_list[0]
            form = BookingForm(room_id=room.id)
            room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)
            context = {
                'room_category': room_category,
                'form': form,
                'room': room,
            }

            return render(request, 'fd_bookings/room_detail.html', context)

        else:
            #   CUSTOM 404
            return HttpResponse('Room category does not exist.')

    @login_required
    def post(self, request, *args, **kwargs):
        room_category = kwargs.get('category', None)
        room_list = Room.objects.filter(category=room_category)
        room = room_list[0]
        form = BookingForm(request.POST, room_id=room.id)

        if form.is_valid() is not True:
            #   CUSTOM 404
            return HttpResponse('Form validation error')  # Need to amend

        data = form.cleaned_data

        if check_availability(room, data['booking_date']) is not True:
            #   CUSTOM 404
            return HttpResponse('Room unavailable')  # Need to amend

        booking = Booking.objects.create(
            user=self.request.user,
            room=room,
            booking_date=data['booking_date'],
            num_passengers=data['num_passengers'],
        )
        booking.save()
        return HttpResponseRedirect('/booking_success')


def booking_success(request):
    # ADD DOCSTRING
    return render(request, 'fd_bookings/booking_success.html',)


@login_required
def amend_booking(request, *args, **kwargs):
    # ADD DOCSTRING
    booking_id = kwargs.get('booking_id')
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'GET':
        form = BookingForm(room_id=booking.room.id)
        context = {
            'booking_id': booking_id,
            'form': form,
            'submitted': False,
            'is_valid': True,
        }
        return render(request, 'fd_bookings/amend_booking.html', context)
    else:
        form = BookingForm(request.POST, room_id=booking.room.id)
        context = {
            'booking_id': booking_id,
            'form': form,
            'submitted': True,
            'is_valid': form.is_valid(),
        }
        if context['is_valid']:
            booking.num_passengers = form.cleaned_data['num_passengers']
            booking.save()
            return HttpResponseRedirect('/booking_success')
        else:
            return render(request, 'fd_bookings/amend_booking.html', context)


# class CancelBooking(generic.DeleteView):
#     # ADD DOCSTRING
#     model = Booking
#     template_name = 'fd_bookings/booking_confirm_delete.html'
#     success_url = reverse_lazy('fd_bookings:ViewBookingList')

@login_required
def cancel_booking(request, *args, **kwargs):
    booking_id = kwargs.get('booking_id')
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking successfully cancelled.")
        return HttpResponseRedirect('/manage_bookings')

    return render(request, 'fd_bookings/booking_confirm_delete.html', {'booking': booking})
