from django.contrib import admin
from .models import Room, Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    Admin UI for the Room model.

    It displays rooms by name, number of beds, and passenger capacity,
    and allows Admin users to filter using those options.
    """
    list_display = ('name', 'beds', 'capacity')
    list_filter = ('name', 'beds', 'capacity')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin UI for the Booking model.

    It displays bookings by user, booking date, room, the number of passengers,
    and when the booking was created/modified.
    Admin users can filter and search for bookings by user, booking date, room
    and the date on which the booking was created.
    """
    list_display = (
        'user',
        'booking_date',
        'room',
        'num_passengers',
        'created_on',
        'modified_on'
        )
    search_fields = ('user', 'email', 'booking_date', 'room', 'created_on')
    list_filter = ('user', 'booking_date', 'room', 'created_on')
