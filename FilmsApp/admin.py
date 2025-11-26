from django.contrib import admin
from .models import Movie, Review, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "country", "rating", "get_genres")
    search_fields = ("title", "country")
    list_filter = ("country", "release_date", "genres")
    filter_horizontal = ("genres",)

    inlines = [ReviewInline]

    def get_genres(self, obj):
        return ", ".join(g.name for g in obj.genres.all())
    get_genres.short_description = "Genres"

    def review_count(self, obj):
        return ", ".join(g.name for g in obj.reviews.all())
    get_genres.short_description = "Genres"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "user_name", "created_at")
    search_fields = ("user_name", "text")
    list_filter = ("created_at", "movie")
    ordering = ("-created_at",)
