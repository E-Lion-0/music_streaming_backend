# Generated by Django 4.2.1 on 2023-06-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_streaming_backend', '0007_remove_playlist_description_customuser_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
