
from django.views.generic.base import View
from .models import Movie
from django.shortcuts import render
# Create your views here.

class MovieView(View):
    #список фильмов
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})







