# Generated by Django 4.2.1 on 2023-06-11 15:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_streaming_backend', '0005_rename_likes_song_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(related_name='liked_songs', to=settings.AUTH_USER_MODEL),
        ),
    ]
