import sys
import os
import django
from datetime import datetime
from pathlib import Path
from django.conf import settings

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
        title = fake.text(max_nb_chars=50)
        content = fake.text(max_nb_chars=500)
        date: datetime = fake.date_this_year()

        django_article.append(
            Post(
                title=title,
                content=content,
                date=date,
            )
        )
    
    if len(django_article) > 0:
        Post.objects.bulk_create(django_article)
