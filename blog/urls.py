from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('artigo/', views.artigo, name='artigo'),
    path('posts/', views.posts, name='posts'),

]