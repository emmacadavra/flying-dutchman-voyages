from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Room, Booking
from .forms import BookingForm


def home_page(request):
    """
    Homepage view.
    """
    return render(request, 'index.html',)


def events_page(request):
    """
    Events page view.
    """
    return render(request, 'events.html',)


def about_page(request):
    """
    About page view.
    """
    return render(request, 'about.html',)


def room_list(request):
    """
    Gathers the data from all rooms and returns them in a list.
    """
    room_list = Room.objects.all()

    context = {
        'room_list': room_list,
    }
    return render(request, 'fd_bookings/our_rooms.html', context)


class ViewBookingList(generic.ListView):
    """
    Retrieves all bookings made by a specific user and returns them in a list.
    If the user is Admin, all bookings made by all users will be returned.
    """
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
    """
    View for individual room details.
    """
    def get(self, request, *args, **kwargs):
        """
        Retrieves the ID of the selected room and returns that room's details
        as well as displaying the booking form.
        """
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
        """
        When a user submits a POST request through the form, this function
        gets the room ID so that the booking form can do its validation
        checks. If the form is valid, and the user is authenticated, the
        booking is created. If the form is not valid, the page updates with
        a validation error to tell the user why it was not valid.
        If the user is not authenticated, they are redirected to a page
        telling them to log in or sign up.
        """
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
    """
    Booking success view.
    """
    return render(request, 'fd_bookings/booking_success.html',)


@login_required
def amend_booking(request, *args, **kwargs):
    """
    Takes the booking ID and feeds it into the template next to the form.
    If the user makes a POST request through the form to amend their booking,
    the form is validated in the same way as the post function under
    RoomDetailView.
    """
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
    """
    Takes the booking ID and retrieves the information. If the user
    confirms they want to cancel their booking, the booking is deleted
    from the database and the user is notified.
    """
    booking_id = kwargs.get('booking_id')
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking successfully cancelled.")
        return HttpResponseRedirect('/manage_bookings')

    return render(
        request,
        'fd_bookings/booking_confirm_delete.html',
        {'booking': booking}
        )


def login_error(request):
    """
    View that appears when a user tries to make a booking but they
    are not logged in.
    """
    return render(request, 'fd_bookings/login_error.html')
