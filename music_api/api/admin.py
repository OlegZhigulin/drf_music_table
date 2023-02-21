from django.contrib import admin

from api.models import Album, AlbumSongNumber, Author, Song


class SongInline(admin.TabularInline):
    model = AlbumSongNumber
    extra = 10


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('year', 'name', 'author')
    inlines = (SongInline,)


class AlbumSongNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'song', 'album')


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumSongNumber, AlbumSongNumberAdmin)
admin.site.register(Song, SongAdmin)
