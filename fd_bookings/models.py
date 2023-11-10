from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('CAP', 'CAPTAIN QUARTERS'),
        ('OCB', 'OFFICER CABIN'),
        ('CRW', 'CREW BUNKS'),
    )

    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    number = models.IntegerField()
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.category} ({self.number}) with {self.beds} bed(s) for {self.capacity} passenger(s).'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    booking_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    num_passengers = models.PositiveSmallIntegerField()
    total_cost = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Booking {self.id} created by {self.user.username}. Room {self.room.category} {self.room.number} for {self.num_passengers} on {self.booking_date}."
