# Create your views here.
from django.shortcuts import render,redirect
# imported our models
from django.core.paginator import Paginator
from . models import music, Audiobooks

def audio(request):
    paginator= Paginator(Audiobooks.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"audio.html",context)

def song(request):
    paginator= Paginator(music.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"music.html",context)
