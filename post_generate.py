def main():
    faker = Faker()
    for i in range(20):
        user = User.objects.get(id=random.choice([1, 2, 3, 5, 6, 7]))
        post = Post.objects.create(author=user, title=faker.sentence(), content=faker.text(),
                                       published=datetime.now().strftime("%Y-%m-%d"), is_active=True)
        post.save()


if __name__ == '__main__':
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    application = get_wsgi_application()

    import random

    from faker import Faker

    from blog.models import Post, User
    from django.utils.timezone import datetime

    main()
