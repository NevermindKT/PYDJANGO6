from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "Films/movie_list.html", {"movies": movies})

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Films/movie_list.html")
    else:
        form = MovieForm()

    return render(request, "Films/add_movie.html", {"form": form})
