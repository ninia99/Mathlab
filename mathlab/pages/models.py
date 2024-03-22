from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category_title = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Tag(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Post(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.ImageField(upload_to='media/', blank=True)
    short_text = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='user_post', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
