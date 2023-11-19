from fd_bookings.models import Room
from .check_availability import check_availability


def get_available_rooms(room_category, booking_date, num_passengers):
    # ADD DOCSTRING
    room_list = Room.objects.filter(category=room_category)

    available_rooms = []

    for room in room_list:
        if check_availability(room, booking_date, num_passengers):
            available_rooms.append(room)
    
    if len(available_rooms) > 0:
         return available_rooms
    else:
         return None
