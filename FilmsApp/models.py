from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    country = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв: {self.movie.title}"