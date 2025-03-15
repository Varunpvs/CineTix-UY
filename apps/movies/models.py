from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False)
    duration = models.IntegerField(help_text="Duration in minutes")
    release_date = models.DateField(null=False, blank=False)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title
