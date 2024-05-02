from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    photo = models.ImageField(upload_to='product_photos', default='default_photo.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    year = models.IntegerField(default=None, null=True)
    views_counter = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров', help_text='Укажите количество просмотров')
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default='')
    published_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            # Проверяем, есть ли в базе данных объект с таким же slug
            # Если есть, добавляем к slug уникальный суффикс
            i = 1
            while Product.objects.filter(slug=self.slug).exists():
                self.slug = slugify(f"{self.name}-{i}")
                i += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/')
    created_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
