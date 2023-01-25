"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#This is the settings.py containing information about the MEDIA_URL and MEDIA_ROOT
from django.conf import settings

#Helps to work with the static files
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from audioplayer import views as audio_views
from . import views 
from blog.views import (
    PostListView,
    PostDetailView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    #####################################
    path('', views.home,name='home'),   
    path('about', views.about,name='about'),
    path('howtouse', views.howtouse,name='howtouse'),
    path('motivation', views.motivation,name='motivation'),
    path('beneficiary', views.beneficiary,name='beneficiary'),
    path('technologies', views.technologies,name='technologies'),
    path('locateme', views.locateme,name='locateme'),
    #######################################
    path('music', audio_views.song, name='music'),
    path('audio', audio_views.audio, name='audio'),
    ######################################
    path('newsfeed/', PostListView.as_view(), name='newsfeed'),
    path('newsfeed/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
