from django.contrib import admin
from django.urls import path
from . import views
from .views import delete_movie, delete_review, movie_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.movie_list, name="movie_list"),
    path("add/", views.add_movie, name="add_movie"),
    path("delete/<int:movie_id>/", delete_movie, name="delete_movie"),
    path("movie/<int:movie_id>/", movie_detail, name="movie_detail"),
    path("review/delete/<int:review_id>/", delete_review, name="delete_review"),
]