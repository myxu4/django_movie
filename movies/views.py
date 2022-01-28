
from django.http import request
from django.views.generic import ListView, DetailView
from .models import Movie
from django.shortcuts import render
# Create your views here.

class MovieView(ListView):
    #список фильмов
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"

class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'
   





