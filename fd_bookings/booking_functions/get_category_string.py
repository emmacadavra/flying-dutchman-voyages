from fd_bookings.models import Room


def get_category_string(room_category):
    room = Room.objects.all()[0]
    room_category = dict(room.ROOM_CATEGORIES).get(room_category, None)

