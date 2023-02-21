from rest_framework import serializers
from django.db import transaction
from api.models import Album, AlbumSongNumber, Author, Song


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('name',)


class AlbumSongSerializer(serializers.ModelSerializer):
    song = serializers.ReadOnlyField(source='song.name')

    class Meta:
        model = AlbumSongNumber
        fields = ('number', 'song')


class AlbumSerializer(serializers.ModelSerializer):
    songs = AlbumSongSerializer(
        many=True,
        source='number_song'
    )
    author = AuthorSerializer()

    class Meta:
        model = Album
        fields = ('author', 'year', 'name', 'songs')

    def create_number_song(self, album, songs_data):
        for obj in songs_data:
            song = Song.objects.get_or_create(name=obj.get('song'))
            AlbumSongNumber.objects.get_or_create(
                number=obj.get('number'),
                song=song[0],
                album=album
            )

    @transaction.atomic
    def create(self, validated_data):
        album_name = validated_data.pop('name', None)
        year = validated_data.pop('year', None)
        author_data = validated_data.pop('author', None)
        create_author = Author.objects.get_or_create(
            name=author_data.get('name')
        )
        album = Album.objects.create(name=album_name, year=year)
        album.author = create_author[0]
        songs_data = self.initial_data.get('songs')
        self.create_number_song(album, songs_data)
        album.save()
        return album
