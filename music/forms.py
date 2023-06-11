from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Song, CustomUser, Album, Playlist, Recommendation, User


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'duration']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'cover_image']


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'detail']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User


class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['song', 'user']