from django.contrib import admin
from .models import Category, Genre, Movie, Actor, Rating, Review, RatingStar, MovieShots

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(MovieShots)
admin.site.register(Review)

# Register your models here.

