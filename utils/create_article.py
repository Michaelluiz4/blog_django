from pathlib import Path
import sys
import os
from django.conf import settings
import django
from datetime import datetime

DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from blog.models import Post

    fake = faker.Faker('pt-BR')

    django_article = []

    for _ in range(10):
        tittle = fake.text(max_nb_chars=50)
        content = fake.text(max_nb_chars=500)
        date: datetime = fake.date_this_year()

        django_article.append(
            Post(
                tittle=tittle,
                content=content,
                date=date,
            )
        )
    
    if len(django_article) > 0:
        Post.objects.bulk_create(django_article)
