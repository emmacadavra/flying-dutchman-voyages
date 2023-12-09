from django.urls import path
from . import views


app_name = 'fd_bookings'

urlpatterns = [
    path('our_rooms/', views.room_list, name='room_list'),
    path('manage_bookings/', views.ViewBookingList.as_view(), name='ViewBookingList'),
    path('room/<room_id>/', views.RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('manage_bookings/amend/<booking_id>/', views.amend_booking, name='amend_booking'),
    path('manage_bookings/cancel/<booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('login_error/', views.login_error, name='login_error'),
]
