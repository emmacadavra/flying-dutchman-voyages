from . import views
from django.urls import path

app_name='fd_bookings'

urlpatterns=[
    path('rooms/', views.RoomList.as_view(), name='rooms'),
    # path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('bookings/', views.BookingView.as_view(), name='bookings')
]