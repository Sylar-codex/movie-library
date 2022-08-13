from django.shortcuts import render,redirect

from .models import Movies
from django.contrib.auth.models import User

def index(request):
    if request.method == 'POST' :
        movies = request.POST['movies']
        status = request.POST['status']
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        obj = Movies(movie_name=movies, status=status,users=user )
        obj.save()
        return redirect("movies:library")

    return render(request, 'movies/index.html')

def library(request):
    current_user = request.user
    watched = Movies.objects.filter(users=current_user.id, status='watched')
    unwatched = Movies.objects.filter(users=current_user.id, status='unwatched')

    return render(request,'movies/library.html', {'watched':watched, 'unwatched':unwatched})
