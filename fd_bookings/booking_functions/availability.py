import datetime
from fd_bookings.models import Room, Booking


def check_availability(room, booking_date):
    available_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking_date == booking.booking_date:
            available_list.append(False)
        else:
            available_list.append(True)
    
    return all(available_list)
