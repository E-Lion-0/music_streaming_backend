from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Song, User


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'duration']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']