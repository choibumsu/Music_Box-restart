from django.urls import path
from . import views

app_name = "musicbox"

urlpatterns = [
    path('', views.musicbox_home, name="musicbox_home"),
    path('search/result', views.search_result, name="search_result"),

    path('<str:kind>', views.kind_list, name="kind_list"),
    path('<str:kind>/<int:pk>', views.kind_detail, name="kind_detail"),
]