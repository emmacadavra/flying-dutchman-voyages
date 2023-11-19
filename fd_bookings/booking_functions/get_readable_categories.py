from fd_bookings.models import Room


def get_readable_categories(room_category):
    room_list = Room.objects.filter(category=room_category)

    if len(room_list)>0:
        room = room_list[0]
        room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)
        return room_category
    else:
        return None
