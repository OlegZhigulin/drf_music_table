# Generated by Django 4.1.7 on 2023-02-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_albumsongnumber_unique_songs_of_album_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Исполнители'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name': 'Песни'},
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(related_name='albums', through='api.AlbumSongNumber', to='api.song'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.TextField(max_length=255, verbose_name='Название альбома'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.TextField(max_length=255, unique=True, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.TextField(max_length=255, unique=True, verbose_name='Название'),
        ),
    ]
