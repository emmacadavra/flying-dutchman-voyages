from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


EVENTS = ((0, "No Event"), (1, "Seasonal Event"), (2, "Easter Sunday Event"))

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()
    num_passengers = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    event = models.IntegerField(choices=EVENTS, default=0)
    total_cost = models.DecimalField()

    def __str__(self):
        return f"Booking {self.id} created by {self.user.username} for {self.booking_date}"
