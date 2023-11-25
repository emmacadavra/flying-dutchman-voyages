from django.contrib import admin
from .models import Room, Booking


# admin.site.register(Room)
# admin.site.register(Booking)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = ('category', 'number', 'beds', 'capacity')
    list_filter = ('category', 'beds', 'capacity')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('user', 'booking_date', 'room', 'num_passengers', 'created_on', 'modified_on')
    search_fields = ('user', 'email', 'booking_date', 'room', 'created_on')
    list_filter = ('user', 'booking_date', 'room', 'created_on')
