from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


# criar uma página onde fica os posts(artigos) do blog
def post(request):
    return 'blog/posts'