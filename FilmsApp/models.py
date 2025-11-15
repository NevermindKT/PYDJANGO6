from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    country = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title