from django.db import models
from django.contrib.auth.models import User

from apps.movies.models import Movie
from apps.theaters.models import Screen

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    seat_number = models.CharField(max_length=10)  # Example: A1, B5
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("Confirmed", "Confirmed"), ("Cancelled", "Cancelled")], default="Confirmed")

    def __str__(self):
        return f"Booking {self.id} - {self.seat_number} ({self.screen.name})"
