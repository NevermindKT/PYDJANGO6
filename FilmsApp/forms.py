from django import forms
from .models import Movie, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'country', 'poster', 'rating']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'text']