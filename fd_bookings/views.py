from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Room, Booking
from .forms import BookingForm
import sweetify


def home_page(request):
    # ADD DOCSTRING
    return render(request, 'index.html',)


def events_page(request):
    # ADD DOCSTRING
    return render(request, 'events.html',)


def about_page(request):
    # ADD DOCSTRING
    return render(request, 'about.html',)


def room_list(request):
    # ADD DOCSTRING
    room_list = Room.objects.all()

    context = {
        'room_list': room_list,
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

    paginate_by = 3


class RoomDetailView(generic.View):
    # ADD DOCSTRINGS
    def get(self, request, *args, **kwargs):
        room_id = kwargs.get('room_id')
        room = get_object_or_404(Room, id=room_id)

        form = BookingForm(room_id=room.id)
        context = {
            'room_name': room.name,
            'form': form,
            'room': room,
        }

        return render(request, 'fd_bookings/room_detail.html', context)

    def post(self, request, *args, **kwargs):
        room_id = kwargs.get('room_id')
        room = get_object_or_404(Room, id=room_id)
        form = BookingForm(request.POST, room_id=room.id)

        if not request.user.is_authenticated:
            return HttpResponseRedirect('/login_error')

        elif form.is_valid():

            data = form.cleaned_data

            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                booking_date=data['booking_date'],
                num_passengers=data['num_passengers'],
            )
            booking.save()
            return HttpResponseRedirect('/booking_success')
        else:
            context = {
                'room_name': room.name,
                'form': form,
                'room': room,
            }
            return render(request, 'fd_bookings/room_detail.html', context)


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
            'booking': booking,
            'booking_id': booking_id,
            'form': form,
        }
        return render(request, 'fd_bookings/amend_booking.html', context)
    else:
        form = BookingForm(request.POST, room_id=booking.room.id)
        context = {
            'booking': booking,
            'booking_id': booking_id,
            'form': form,
            'is_valid': form.is_valid(),
        }

        if context['is_valid']:
            booking.booking_date = form.cleaned_data['booking_date']
            booking.num_passengers = form.cleaned_data['num_passengers']
            booking.save()
            return HttpResponseRedirect('/booking_success')
        else:
            return render(request, 'fd_bookings/amend_booking.html', context)


@login_required
def cancel_booking(request, *args, **kwargs):
    booking_id = kwargs.get('booking_id')
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        sweetify.success(request, "Booking successfully cancelled.")
        return HttpResponseRedirect('/manage_bookings')

    return render(request, 'fd_bookings/booking_confirm_delete.html', {'booking': booking})


def login_error(request):
    return render(request, 'fd_bookings/login_error.html')
