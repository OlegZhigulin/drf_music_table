from django.db import models


class Author(models.Model):
    name = models.TextField(
        verbose_name="Исполнитель",
        unique=True,
        max_length=255
    )

    class Meta:
        verbose_name = 'Исполнители'

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.TextField(
        verbose_name='Название',
        unique=True,
        max_length=255
    )

    class Meta:
        verbose_name = 'Песни'

    def __str__(self):
        return self.name


class Album(models.Model):
    year = models.SmallIntegerField(verbose_name='Год выпуска')
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
        )
    name = models.TextField(
        'Название альбома',
        max_length=255
        )
    songs = models.ManyToManyField(
        Song,
        through='AlbumSongNumber',
        through_fields=('album', 'song'),
        related_name='albums'
    )

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['id']
        constraints = (
            models.UniqueConstraint(
                fields=['name', 'author'],
                name='unique_album_of_author'),
        )

    def __str__(self):
        return self.name


class AlbumSongNumber(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name='Порядковый номер',
        help_text='Должно быть целое положительное число'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='number_song'
    )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни в альбоме'
        ordering = ['id']
        constraints = (
            models.UniqueConstraint(
                fields=['song', 'album'], name='unique_songs_of_album'),
        )

    def __str__(self):
        return f'{self.album} {self.song}'
