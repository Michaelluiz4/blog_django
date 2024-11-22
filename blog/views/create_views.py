from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def artigo(request):
    artigos = Post.objects.all().order_by('-id')

    context = {
        'artigos': artigos
    }

    return render(request, 'blog/artigos.html', context)


# criar uma views onde mostra os post individual
def posts(request):
    return render(request, 'blog/posts.html')