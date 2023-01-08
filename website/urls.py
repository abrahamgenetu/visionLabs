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
from django.urls import path

#This is the settings.py containing information about the MEDIA_URL and MEDIA_ROOT
from django.conf import settings

#Helps to work with the static files
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #####################################
    path('', views.home,name='home'),   
    path('about', views.about,name='about'),
    path('howtouse', views.howtouse,name='howtouse'),
    path('motivation', views.motivation,name='motivation'),
    path('beneficiary', views.beneficiary,name='beneficiary'),
    path('technologies', views.technologies,name='technologies'),
    # path('audiobooks', views.audiobooks,name='audiobooks'),
    
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)