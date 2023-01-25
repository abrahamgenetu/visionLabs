from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
)
from . import views

urlpatterns = [
    path('newsfeed', PostListView.as_view(), name='newsfeed'),
    path('newsfeed/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
