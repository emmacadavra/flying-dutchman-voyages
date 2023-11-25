from django.contrib import admin
from .models import Room, Booking


# admin.site.register(Room)
# admin.site.register(Booking)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display =
    search_fields =
    list_filter =

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display =
    search_fields =
    list_filter =
