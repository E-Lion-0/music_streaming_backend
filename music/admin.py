from django.apps import AppConfig
from django.contrib import admin

from .models import Artist, Album, Song, CustomUser, Playlist, Recommendation


# Register your models here.

class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin'


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(CustomUser)
admin.site.register(Playlist)
admin.site.register(Recommendation)
