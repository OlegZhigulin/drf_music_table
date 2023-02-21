from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (
    AlbumViewSet,
    AuthorViewSet,
    SongViewSet,
)

router = SimpleRouter()

router.register('authors', AuthorViewSet)
router.register('songs', SongViewSet)
router.register('albums', AlbumViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
