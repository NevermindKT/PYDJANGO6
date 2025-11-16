from django.urls import path
from . import views
from .views import delete_movie

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("add/", views.add_movie, name="add_movie"),
    path("delete/<int:movie_id>/", delete_movie, name="delete_movie"),
]