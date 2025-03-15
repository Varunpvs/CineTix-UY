from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.movies.views import MoviesView, MovieDetailView

urlpatterns = [
    path(
        "movies/",
        login_required(MoviesView.as_view(template_name="movies_list.html")),
        name="movies-list",
    ),
    path(
        "movie/<int:id>/",
        login_required(MovieDetailView.as_view(template_name="movie_detail.html")),
        name="movie-detail",
    ),
]


