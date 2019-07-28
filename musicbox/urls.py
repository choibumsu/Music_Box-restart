from django.urls import path
from . import views

app_name = "musicbox"

urlpatterns = [
    path('', views.musicbox_home, name="musicbox_home"),
    path('song/', views.song_list, name="song_list"),
]