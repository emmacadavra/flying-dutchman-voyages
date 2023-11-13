from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('CAP', 'CAPTAIN\'S QUARTERS'),
        ('OCD', 'DOUBLE CABIN'),
        ('OCS', 'SINGLE CABIN'),
        ('CRW', 'CREW BUNKS'),
    )

    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
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

    def get_category_name(self):
        room_categories = dict({self.room.ROOM_CATEGORIES})
        room_category = room_categories.get(self.room.category)
        return room_category

    def __str__(self):
        return f"Booking {self.id} created by {self.user.username}. Room {self.room} on {self.booking_date}"
