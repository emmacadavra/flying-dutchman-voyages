from fd_bookings.models import Room
from django.urls import reverse, reverse_lazy


def get_room_category_urls():
    # ADD DOCSTRING
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)
    room_category_urls = []

    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('fd_bookings:RoomDetailView', kwargs={'category': room_category})
        
        room_category_urls.append((room, room_url))
    
    return room_category_urls