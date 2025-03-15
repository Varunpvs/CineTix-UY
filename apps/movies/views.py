from django.views.generic import TemplateView

from apps.movies.models import Movie
from web_project import TemplateLayout


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to academy/urls.py file for more pages.
"""


class MoviesView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        approved_movies = Movie.objects.filter(poll__decision=True)
        context['movies'] = approved_movies
        return context


from django.http import Http404
from django.shortcuts import get_object_or_404

class MovieDetailView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # Initialize the global layout
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Get the movie ID from the URL parameters (as part of the path)
        movie_id = kwargs.get('id')

        try:
            # Get the movie object using the provided ID
            movie = get_object_or_404(Movie, pk=movie_id)
            context['movie'] = movie
        except Movie.DoesNotExist:
            raise Http404("Movie not found.")

        return context

