from django.shortcuts import render, get_object_or_404
from .models import Song, Artist, Album, Group


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

