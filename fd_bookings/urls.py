from django.urls import path
from . import views


app_name = 'fd_bookings'

urlpatterns = [
    path('our_rooms/', views.room_list, name='room_list'),
    path('manage_bookings/', views.ViewBookingList.as_view(), name='ViewBookingList'),
    path('room/<category>', views.RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('manage_bookings/amend/<booking_id>', views.amend_booking, name='amend_booking'),
    path('manage_bookings/cancel/<pk>', views.CancelBooking.as_view(), name='CancelBooking'),
]
