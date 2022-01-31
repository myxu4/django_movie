
from django.http import request
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie
from django.shortcuts import redirect, render
from .forms import ReviewForm
# Create your views here.

class MovieView(ListView):
    #список фильмов
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"

class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    #Класс оставления отзывов
    
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parents_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

   





