from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.


def movie(request):
    movies = Movie.objects.all()

    return render(request, 'movie/list.html', {"movies": movies})


def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)

    return render(request, 'movie/detail.html', {"movie": movie})


def movie_search(request):
    q = request.POST.get('q', " ")
    if q:
        movies = Movie.objects.filter(title__icontains=q)
        return render(request, 'movie/search.html', {'movies': movies, 'q': q})
    else:
        return render(request, 'movie/search.html')
