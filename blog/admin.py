from django.contrib import admin
from blog import models

# Register your models here.

@admin.register(models.Post)
class PostBlog(admin.ModelAdmin):
    list_display = 'tittle', 'date',
    ordering = '-id',
    search_fields = 'tittle',
    list_filter = 'date',
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = 'tittle',
