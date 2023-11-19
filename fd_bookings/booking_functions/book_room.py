from fd_bookings.models import Room, Booking

def book_room():
    if len(available_rooms) > 0:
        booking = Booking.objects.create(
        user = self.request.user,
        room = room,
        booking_date = data['booking_date'],
        num_passengers = data['num_passengers']
    )
    booking.save()