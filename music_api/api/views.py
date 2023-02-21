from rest_framework import viewsets

from api.models import Album, Author, Song
from api.serializers import (
    AlbumSerializer,
    AuthorSerializer,
    SongSerializer
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.prefetch_related(
        'songs'
    ).select_related(
        'author'
    ).all()
    serializer_class = AlbumSerializer
