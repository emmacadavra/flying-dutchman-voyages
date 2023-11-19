from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from cloudinary.models import CloudinaryField


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('CAPQ', 'Captain\'s Quarters'),
        ('DCBN', 'Double Cabin'),
        ('SCBN', 'Single Cabin'),
        ('CRWH', 'Crew Hammocks'),
    )

    category = models.CharField(max_length=4, choices=ROOM_CATEGORIES)
    number = models.IntegerField()
    beds = models.IntegerField()
    capacity = models.IntegerField()
    room_cost = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    # room_image = 

    def __str__(self):
        return f'{self.category} ({self.number}) with {self.beds} bed(s) for {self.capacity} passenger(s)'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    booking_date = models.DateField()
    # booking_date = models.DateField(validators=[validate_sun])
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True)
    num_passengers = models.PositiveSmallIntegerField()
    # total_cost = models.DecimalField(decimal_places=2, max_digits=10)

    # def validate_sun(value):
    #     if value is not 1

    def __str__(self):
        return f"Booking {self.id} created by {self.user.username}. Room {self.room} on {self.booking_date}"


    def get_room_name(self):
        room_categories = dict(self.room.ROOM_CATEGORIES)
        room_category = room_categories.get(self.room.category)
        return room_category
    
    def get_cancel_booking(self):
        return reverse_lazy('fd_bookings:CancelBooking', args=[self.pk])
