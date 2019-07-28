from django.shortcuts import render, get_object_or_404
from .models import Song, Artist, Genre, Playlist

# Create your views here.
def musicbox_home(request):
    context = {
        'song_count' : Song.objects.all().count(), 
        'artist_count' : Artist.objects.all().count(),
        'genre_count' : Genre.objects.all().count(),
        'playlist_count' : Playlist.objects.all().count(),
    }
    return render(request, "musicbox/musicbox_home.html", context=context)

def song_list(request):
    songs = Song.objexts.all()
    return render(request, "musicbox/song_list.html", {
        "songs" : songs,
    })

