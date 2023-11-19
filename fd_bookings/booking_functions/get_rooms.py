from fd_bookings.models import Room
from django.urls import reverse, reverse_lazy


def get_rooms():
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)
    room_list = []

    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('fd_bookings:RoomDetailView', kwargs={'category': room_category})
        
        room_list.append((room, room_url))
    
    return room_list