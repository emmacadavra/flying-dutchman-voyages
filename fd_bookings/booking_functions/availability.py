import datetime
from fd_bookings.models import Room, Booking


def check_availability(room, booking_date):
    available_list = []
    booking_list = Booking.objects.filter(room=room)
    
