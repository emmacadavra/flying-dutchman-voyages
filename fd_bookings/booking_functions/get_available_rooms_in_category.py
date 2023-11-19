from fd_bookings.models import Room


def get_available_rooms_in_category(category):
    room_list = Room.objects.filter(category=room_category)

    if len(room_list)>0:
        room = room_list[0]
        room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)
        context = {
            'room_category': room_category,
            'form': form,
            'room': room,
        }
        return render(request, 'fd_bookings/room_detail.html', context)
    else:
# NEED TO UPDATE THIS TO BETTER RESPONSES/REDIRECTS
        return HttpResponse('Room category does not exist.')
