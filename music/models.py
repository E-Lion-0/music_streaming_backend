from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Custom fields and additional modifications
    username = models.CharField(max_length=20)
    bio = models.TextField(blank=True)
    favorite_genre = models.CharField(max_length=100, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_users'  # Added related_name argument
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users'  # Added related_name argument
    )

    class Meta:
        app_label = "music_streaming_backend"


class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    photo = models.ImageField(upload_to='artists/', blank=True)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "music_streaming_backend"


class Band(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Artist)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='groups/')
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "music_streaming_backend"


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True, blank=True)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/')
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "music_streaming_backend"


User = get_user_model()


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()
    liked = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='liked_songs')

    def __str__(self):
        return self.title

    def toggle_like(self, user):
        if user in self.liked.all():
            self.likes.remove(user)
        else:
            self.likes.add(user)

    class Meta:
        app_label = "music_streaming_backend"


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "music_streaming_backend"


class Recommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f"{self.user.username} recommends {self.song.title}"
