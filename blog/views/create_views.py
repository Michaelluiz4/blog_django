from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator


# Create your views here.

def index(request):

    context = {

    }

    return render(request, 'blog/index.html', context)


def artigos(request):
    artigos = Post.objects.all().order_by('-id')

    paginator = Paginator(artigos, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'blog/artigos.html', context)


# criar uma views onde mostra os post individual
def posts(request):

    context = {

    }

    return render(request, 'blog/posts.html', context)