from django.shortcuts import render, get_object_or_404, redirect


from .forms import SongForm
from .models import Song, Artist, Album, Group
from django.contrib.auth.decorators import login_required


def home(request):
    # Retrieve the list of liked songs and artists
    liked_songs = Song.objects.filter(liked=True)
    liked_artists = Artist.objects.filter(liked=True)

    context = {
        'liked_songs': liked_songs,
        'liked_artists': liked_artists,
    }
    return render(request, 'home.html', context)


def is_artist_or_group(user):
    return user.is_authenticated and (user.is_artist or user.is_group)


@login_required
def add_song(request):
    if not is_artist_or_group(request.user):
        return redirect('home')  # Redirect to home if the user is not an artist or group

    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the desired page after successful song addition
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
    return render(request, 'music/artist_detail.html', {'artist': artist})


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})


def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/album_detail.html', {'album': album})


