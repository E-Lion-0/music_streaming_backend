# Generated by Django 4.2.1 on 2023-06-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_streaming_backend', '0006_song_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='description',
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_genre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='playlist',
            name='detail',
            field=models.TextField(blank=True),
        ),
    ]
