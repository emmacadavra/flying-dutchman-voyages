from fd_bookings.models import Booking


def check_availability(room, booking_date):
    # ADD DOCSTRING
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking_date == booking.booking_date:
            return False
        else:
            return True
