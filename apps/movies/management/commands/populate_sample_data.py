from django.core.management.base import BaseCommand
from django.utils.timezone import now
from apps.theaters.models import Theater, Screen
from apps.movies.models import Movie
from apps.polls.models import Poll

class Command(BaseCommand):
    help = "Populate sample data for theaters, screens, and polls"

    def handle(self, *args, **kwargs):
        # Step 1: Create Theaters
        theater1, _ = Theater.objects.get_or_create(name="Grand Cinema", location="Main Street")
        theater2, _ = Theater.objects.get_or_create(name="Galaxy Theater", location="Downtown")

        # Step 2: Create Screens
        screen1, created1 = Screen.objects.get_or_create(theater=theater1, name="Screen 1", total_rows=8, total_columns=10)
        screen2, created2 = Screen.objects.get_or_create(theater=theater2, name="Screen 2", total_rows=6, total_columns=8)

        # Step 3: Generate Seat Layouts (Blocking seats initially)
        if created1:
            screen1.generate_seats(block_all=True)
        if created2:
            screen2.generate_seats(block_all=True)

        # Step 4: Add a Movie (Fixing missing release_date)
        movie, _ = Movie.objects.get_or_create(
            title="The Dark Knight",
            defaults={
                "duration": 152,  # Example duration in minutes
                "release_date": now().date()  # Fix: Add a valid release date
            }
        )

        # Step 5: Create a Poll for the movie
        poll, created_poll = Poll.objects.get_or_create(movie=movie, defaults={"threshold": 50})

        # Step 6: Print Success Message
        self.stdout.write(self.style.SUCCESS("Sample data has been populated successfully!"))
