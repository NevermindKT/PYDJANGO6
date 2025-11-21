from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import MovieForm, ReviewForm


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Films/movie_list.html")
    else:
        form = MovieForm()

    return render(request, "Films/add_movie.html", {"form": form})

def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect("Films/movie_list.html")

def movie_list(request):
    movies = Movie.objects.all().order_by("-id")
    return render(request, "Films/movie_list.html", {"movies": movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all().order_by("-created_at")

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect("Films/movie_detail.html", movie_id=movie.id)
    else:
        form = ReviewForm()

    return render(request, "Films/movie_detail.html", {
        "movie": movie,
        "reviews": reviews,
        "form": form
    })

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    movie_id = review.movie.id
    review.delete()
    return redirect("Films/movie_detail.html", movie_id=movie_id)