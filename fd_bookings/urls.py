from .views import RoomList, BookingList
from django.urls import path

app_name='fd_bookings'

urlpatterns=[
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
]