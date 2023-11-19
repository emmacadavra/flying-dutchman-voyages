from django.urls import path
from . import views


app_name='fd_bookings'

urlpatterns=[
    path('our_rooms/', views.RoomList, name='RoomList'),
    path('manage_bookings/', views.ViewBookingList.as_view(), name='ViewBookingList'),
    path('room/<category>', views.RoomDetailView.as_view(), name='RoomDetailView'),
    path('manage_bookings/edit/<pk>', views.EditBooking.as_view(), name='EditBooking'),
    path('manage_bookings/cancel/<pk>', views.CancelBooking.as_view(), name='CancelBooking'),
]