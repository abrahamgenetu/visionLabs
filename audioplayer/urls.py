from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "audioplayer"


urlpatterns = [
    path("audio", views.audio, name="audio"),
    path("music", views.song, name="music"),
]
