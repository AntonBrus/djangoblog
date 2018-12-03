from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Tags class
class Tag(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    # Чтобы при отображении объекта целиком, показывалось определенное поле
    def __str__(self):
        return self.title


# Article class
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(default='default.png', blank=True)
    # Автор статьи
    author = models.ForeignKey(User, default='1', on_delete=models.DO_NOTHING)
    # Теги
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def part_text(self):
        return self.body[:70] + '...'

    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url


# Comment class
class Comment(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:100] + '...'


