# Generated by Django 4.2.1 on 2023-06-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_streaming_backend', '0003_rename_likes_song_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='liked',
        ),
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.BooleanField(default=False),
        ),
    ]
