
from http import HTTPStatus
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from ..models import Album, Author, Song, AlbumSongNumber

User = get_user_model()


class PostPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = Author.objects.create(name='Багровый Фантомас')
        cls.song = Song.objects.create(name='Золотые Жирафы')
        cls.album = Album.objects.create(
            author=cls.author,
            name='Вчерашний хлеб',
            year=2022
        )
        cls.album_with_song1 = AlbumSongNumber.objects.create(
            number=1,
            album=cls.album,
            song=cls.song
        )


    def setUp(self):
        self.client = APIClient()

    def test_author(self):
        response = self.client.get('/api/author/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json()[0].get('name'), 'Багровый Фантомас')
    
    def test_song(self):
        response = self.client.get('/api/song/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json()[0].get('name'), 'Золотые Жирафы')    

    def test_album(self):
        response = self.client.get('/api/album/')
        print(response.json())
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json()[0].get('name'), 'Вчерашний хлеб')
        self.assertEqual(response.json()[0].get('author').get('name'), 'Багровый Фантомас')
        self.assertEqual(response.json()[0].get('year'), 2022)
        