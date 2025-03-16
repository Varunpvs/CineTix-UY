



from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView

from apps.movies.models import Movie
from apps.bookings.models import Booking
from apps.theaters.models import Screen
from apps.polls.models import Poll
import json
from web_project import TemplateLayout
import ast

class BookMovieView(LoginRequiredMixin, TemplateView):
    template_name = "book_movie.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        movie = get_object_or_404(Movie, id=self.kwargs['movie_id'])
        poll = get_object_or_404(Poll, movie=movie)

        # Debugging
        print(f"Fetching booking context for movie: {movie.title}")

        screen = get_object_or_404(Screen, theater=poll.screen.theater)

        # Convert seat layout with Python booleans to JavaScript booleans (True/False to true/false)
        seat_layout = screen.seat_layout

        # Debugging
        print(f"Screen found: {screen.name} with seat layout: {seat_layout}")
        print(json.dumps(seat_layout))
        context.update({
            "movie": movie,
            "screen": screen,
            "seat_layout": json.dumps(seat_layout),  # Now it's ready to be used in JavaScript
        })
        return context

    def post(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, id=self.kwargs['movie_id'])
        poll = get_object_or_404(Poll, movie=movie)  # Get the poll here
        screen = get_object_or_404(Screen, theater=poll.screen.theater)  # Use the screen from the poll's theater
        selected_seats_string = request.POST.get("selected_seats") # get as string

        # Debugging
        print(f"User {request.user} attempting to book seats: {selected_seats_string} for movie {movie.title}")

        if not selected_seats_string:
            messages.error(request, "Please select at least one seat.")
            return redirect("book-movie", movie_id=movie.id)

        selected_seats = selected_seats_string.split(",") # split into individual seat strings.
        print(selected_seats)

        for seat in selected_seats:
            print(seat)
            row, col = seat.split("-")
            print(row, col)
            try:
                print(screen.seat_layout)
                if not screen.seat_layout[row][col]:
                    messages.error(request, f"Seat {seat} is already booked.")
                    return redirect("book-movie", movie_id=movie.id)
                screen.seat_layout[row][col] = False  # Mark as booked
            except(IndexError, ValueError):
                messages.error(request, f"Seat {seat} is invalid")
                return redirect("book-movie", movie_id=movie.id)
        screen.save()

        # Debugging
        print(f"Seats booked successfully: {selected_seats}")

        Booking.objects.create(user=request.user, movie=movie, screen=screen, seat_number=selected_seats)
        messages.success(request, "Booking successful!")
        return redirect("user-bookings")




class UserBookingsView(LoginRequiredMixin, TemplateView):
    template_name = "list-bookings.html"

    def get_context_data(self, **kwargs):
        import ast
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        bookings = Booking.objects.filter(user=self.request.user)
        for booking in bookings:
            booking.seat_number = ast.literal_eval(booking.seat_number)
        context["bookings"] = bookings

        # Debugging
        print(f"User {self.request.user} has {len(context['bookings'])} bookings.")

        return context


class CancelBookingView(LoginRequiredMixin, APIView):

    def post(self, request, *args, **kwargs):
        booking = get_object_or_404(Booking, id=self.kwargs['booking_id'], user=request.user)
        screen = booking.screen

        # Debugging
        print(f"User {request.user} canceling booking ID {booking.id} for seats: {booking.seat_number}")

        for seat in ast.literal_eval(booking.seat_number):
            row, col = seat.split("-")
            screen.seat_layout[row][col] = True  # Mark seat as available again
        screen.save()

        booking.status = "canceled"
        booking.save()
        messages.success(request, "Booking canceled successfully.")

        # Debugging
        print(f"Booking {booking.id} canceled successfully.")

        return redirect("user-bookings")
