from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Room(models.Model):
    """
    Creates the fields available for Admin users when entering room details,
    and stores the information in the database.
    """
    name = models.CharField(max_length=200, unique=True)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    summary = models.CharField(max_length=500, null=True)
    description = models.TextField()
    room_cost = models.DecimalField(decimal_places=2, max_digits=9, null=True)
    room_image_1 = CloudinaryField('image', default='placeholder1')
    room_image_2 = CloudinaryField('image', default='placeholder2')
    room_image_3 = CloudinaryField('image', default='placeholder3')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.beds} bed(s) for up to {self.capacity} passenger(s))'


class Booking(models.Model):
    """
    Handles information from user bookings and stores it in the database.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    booking_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True)
    num_passengers = models.PositiveSmallIntegerField()
    total_cost = models.DecimalField(decimal_places=2, max_digits=9, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Booking {self.id} created by {self.user.username} ({self.room} on {self.booking_date})"
