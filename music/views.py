from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, get_user_model
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SongForm, SignUpForm, PlaylistForm, RecommendationForm
from .models import Song, Artist, Album, Recommendation, CustomUser, Playlist

User = get_user_model()


def home(request):
    liked_songs = Song.objects.filter(liked=True)
    liked_artists = Artist.objects.filter(liked=True)
    artists = Artist.objects.all()
    albums = Album.objects.all()
    recommendations = Recommendation.objects.all()

    context = {
        'artists': artists,
        'liked_songs': liked_songs,
        'liked_artists': liked_artists,
        'albums': albums,
        'recommendations': recommendations,
    }
    return render(request, 'home.html', context)


def is_artist_or_group(user):
    return user.is_authenticated and (user.is_artist or user.is_group)


@login_required
def add_song(request):
    if not is_artist_or_group(request.user):
        return redirect('home')

    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form})


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})


def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'music/song_detail.html', {'song': song})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})


def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'artist_page.html', {'artist': artist})


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})


def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'album_page.html', {'album': album})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class ArtistCreateView(CreateView):
    model = Artist
    fields = ['name', 'biography', 'photo', 'liked']
    template_name = 'artist/artist_create.html'
    success_url = reverse_lazy('artist_create')


class ArtistForm:
    pass


def create_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm()
    return render(request, 'create_artist.html', {'form': form})


class AlbumForm:
    pass


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'create_album.html', {'form': form})


class AlbumCreateView(CreateView):
    model = Album
    fields = ['title', 'artist', 'release_date', 'cover_image', 'liked']
    template_name = 'album/templates/music/create_album.html'
    success_url = reverse_lazy('album_create')


class SongCreateView(CreateView):
    model = Song
    fields = ['title', 'album', 'duration', 'liked']
    template_name = 'song/song_create.html'
    success_url = reverse_lazy('song_create')


def create_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'create_song.html', {'form': form})


@login_required
def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.owner = request.user
            playlist.save()
            form.save_m2m()
            return redirect('playlist_detail', playlist_id=playlist.pk)
    else:
        form = PlaylistForm()
    return render(request, 'playlist_create.html', {'form': form})


def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    return render(request, 'playlist_detail.html', {'playlist': playlist})


def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    playlist_set = user.playlist_set.all()
    return render(request, 'user_profile.html', {'user': user, 'playlist_set': playlist_set})


def create_recommendation(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.song = song
            recommendation.save()
            return redirect('song_detail', song_id=song.pk)
    else:
        form = RecommendationForm()
    return render(request, 'create_recommendation.html', {'form': form, 'song': song})


def search(request):
    query = request.GET.get('query')
    if query:
        songs = Song.objects.filter(Q(title__icontains=query))
        albums = Album.objects.filter(Q(title__icontains=query))
        artists = Artist.objects.filter(Q(name__icontains=query))
        return render(request, 'search.html', {'query': query, 'songs': songs, 'albums': albums, 'artists': artists})
    else:
        return render(request, 'search.html', {'query': query})


def toggle_like(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.user.is_authenticated:
        song.toggle_like(request.user)
        return JsonResponse({'status': 'success', 'liked': song.likes.filter(id=request.user.id).exists()})
    else:
        return JsonResponse({'status': 'error', 'message': 'User is not authenticated.'})
