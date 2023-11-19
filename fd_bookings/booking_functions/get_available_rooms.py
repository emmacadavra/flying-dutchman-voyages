from fd_bookings.models import Room
from fd_bookings.booking_functions.check_availability import check_availability


def get_available_rooms(room_category, form):
    room_list = Room.objects.filter(category=room_category)

    if form.is_valid():
            data = form.cleaned_data

    available_rooms = []

    for room in room_list:
        if check_availability(room, data['booking_date']):
            available_rooms.append(room)
    
    if len(available_rooms) > 0:
         return available_rooms
    else:
         return None
