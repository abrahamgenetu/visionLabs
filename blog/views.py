from django.shortcuts import render
from django.views.generic import (
    DetailView,ListView,
)
from .models import Post


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


