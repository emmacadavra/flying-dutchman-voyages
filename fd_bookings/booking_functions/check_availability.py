from fd_bookings.models import Booking


def check_availability(room, booking_date):
    """
    Checks the user's requested booking date against
    all existing booked dates for that room.
    """
    booking_list = Booking.objects.filter(room=room)

    if len(booking_list) == 0:
        return True

    valid = True

    for booking in booking_list:
        if booking_date == booking.booking_date:
            valid = False
            break

    return valid
