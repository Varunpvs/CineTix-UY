from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.bookings.views import BookMovieView, UserBookingsView, CancelBookingView

urlpatterns = [
    path("book/<int:movie_id>/", login_required(BookMovieView.as_view()), name="book-movie"),
    path("my-bookings/", login_required(UserBookingsView.as_view()), name="user-bookings"),
    path("cancel-booking/<int:booking_id>/", login_required(CancelBookingView.as_view()), name="cancel-booking"),
]
