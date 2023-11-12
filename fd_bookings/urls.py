from django.urls import path
from . import views


app_name='fd_bookings'

urlpatterns=[
    path('our_rooms/', views.RoomList.as_view(), name='our_rooms'),
    path('view_bookings/', views.ViewBookingList.as_view(), name='view_bookings'),
    path('room_detail/', views.BookingView.as_view(), name='make_booking'),
    # path('room/<category>', views.RoomDetailView.as_view(), name='room_detail'),
]