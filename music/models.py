import django.db
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    photo = models.ImageField(upload_to='artists/', blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Artist)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='groups/')

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/')

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title
