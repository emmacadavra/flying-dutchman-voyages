from fd_bookings.models import Room


def get_available_rooms(room_category, form):
    room_list = Room.objects.filter(category=room_category)

    if form.is_valid():
            data = form.cleaned_data

    available_rooms = []

    for room in room_list:
        if check_availability(room, data['booking_date']):
            available_rooms.append(room)
