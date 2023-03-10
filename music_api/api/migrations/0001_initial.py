# Generated by Django 4.1.7 on 2023-02-20 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField(verbose_name='Год выпуска')),
                ('name', models.TextField(verbose_name='Название альбома')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Исполнитель')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumSongNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(help_text='Должно быть целое положительное число', verbose_name='Порядковый номер')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_song', to='api.album')),
                ('song_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.song')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни в альбоме',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.author'),
        ),
        migrations.AddConstraint(
            model_name='albumsongnumber',
            constraint=models.UniqueConstraint(fields=('song_title', 'album'), name='unique_songs_of_album'),
        ),
        migrations.AddConstraint(
            model_name='album',
            constraint=models.UniqueConstraint(fields=('name', 'author'), name='unique_album_of_author'),
        ),
    ]
