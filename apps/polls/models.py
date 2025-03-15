from django.db import models
from django.conf import settings

class Poll(models.Model):
    movie = models.OneToOneField(
        "movies.Movie", on_delete=models.CASCADE, null=True, blank=True
    )
    theater = models.ForeignKey(
        "theaters.Theater", on_delete=models.CASCADE, null=True, blank=True
    )
    screen = models.ForeignKey(
        "theaters.Screen", on_delete=models.CASCADE, null=True, blank=True
    )
    yes_votes = models.PositiveIntegerField(default=0)
    threshold = models.PositiveIntegerField(default=50, help_text="Minimum votes required to approve movie")
    decision = models.BooleanField(default=None, null=True, blank=True, help_text="True if movie will be released")

    def vote(self):
        """Records a 'Yes' vote"""
        self.yes_votes += 1
        self.save()
        self.finalize_poll()

    def finalize_poll(self):
        """Finalizes the poll if yes_votes reach the threshold"""
        if self.yes_votes >= self.threshold:
            self.decision = True
            self.save()
            if self.screen:
                self.screen.open_seat_booking()

    def __str__(self):
        return f"Poll for {self.movie.title if self.movie else 'Unknown Movie'} - {'Approved' if self.decision else 'Pending'}"

class PollVote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True)
    vote = models.BooleanField(default=True)  # True for 'Yes', False for 'No'

    class Meta:
        unique_together = ('user', 'poll')  # Ensure a user can vote only once per poll

    def __str__(self):
        return f"Vote of {self.user.username if self.user else 'Unknown User'} for {self.poll.movie.title if self.poll.movie else 'Unknown Movie'}"
