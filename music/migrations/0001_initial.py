# Generated by Django 4.2.1 on 2023-06-05 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music_streaming_backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_streaming_backend.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_streaming_backend.customuser')),
            ],
        ),
    ]
