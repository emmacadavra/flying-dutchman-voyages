from django.urls import path
from . import views


app_name='fd_bookings'

urlpatterns=[
    path('room_list/', views.RoomList.as_view(), name='room_list'),
    path('booking_list/', views.BookingList.as_view(), name='booking_list'),
    path('make_booking/', views.BookingView.as_view(), name='make_booking'),
]