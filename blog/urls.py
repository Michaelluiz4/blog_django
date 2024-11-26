from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/artigos/', views.artigos, name='artigos'),
    path('posts/', views.posts, name='posts'),

]