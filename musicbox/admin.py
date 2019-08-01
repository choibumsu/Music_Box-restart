from django.contrib import admin
from .models import Genre, Artist, Song, Playlist

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'real_name', 'another_name']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre']

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name']