from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(default=timezone.now)


    def __str__(self):
        return f'{self.title}'
