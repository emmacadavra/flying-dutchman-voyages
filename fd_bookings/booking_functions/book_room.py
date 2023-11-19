from fd_bookings.models import Room, Booking

def book_room(request, room, booking_date, num_passengers):
        booking = Booking.objects.create(
            user = request.user,
            room = room,
            booking_date = booking_date,
            num_passengers = num_passengers,
        )
        booking.save()

        return booking