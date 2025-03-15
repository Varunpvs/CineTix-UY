from django.db import models

class Theater(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Screen(models.Model):
    theater = models.ForeignKey(
        Theater, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=50)
    total_rows = models.IntegerField(default=10)
    total_columns = models.IntegerField(default=12)
    seat_layout = models.JSONField(default=dict, blank=True)
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.SET_NULL, null=True, blank=True
    )
    bookings_open = models.BooleanField(default=False)

    def generate_seats(self, block_all=True):
        """ Generate seat layout where all seats are initially blocked """
        layout = {
            chr(65 + row): {str(col + 1): not block_all for col in range(self.total_columns)}
            for row in range(self.total_rows)
        }
        self.seat_layout = layout
        self.save()

    def open_seat_booking(self):
        """ Open bookings only if the poll decision is True """
        from apps.polls.models import Poll  # Import inside function to avoid circular import

        poll = Poll.objects.filter(movie=self.movie).first()
        if poll and poll.decision:
            layout = self.seat_layout
            for row in layout:
                for col in layout[row]:
                    layout[row][col] = True  # Set all seats to available
            self.seat_layout = layout
            self.bookings_open = True
            self.save()
        else:
            raise ValueError("Poll not approved! Cannot open bookings.")

    def __str__(self):
        return f"{self.name} ({self.total_rows} rows x {self.total_columns} seats)"
