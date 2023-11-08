from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    booking_date = models.DateField()
    num_passengers = models.PositiveSmallIntegerField()
    # event = choices?
    total_cost = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Booking {self.id} created by {self.user.username} for {self.booking_date}"
