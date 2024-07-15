from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings

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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products', null=True)
    updated_at = models.DateTimeField(auto_now=True)
    year = models.IntegerField(default=None, null=True)
    views_counter = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров', help_text='Укажите количество просмотров')
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    published_at = models.DateTimeField(default=timezone.now)
    available = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            i = 1
            while Product.objects.filter(slug=self.slug).exists():
                self.slug = slugify(f"{self.name}-{i}")
                i += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_change_any_description", "Can change any description"),
            ("can_change_any_category", "Can change any category"),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE)
    version_number = models.CharField(max_length=50)
    version_name = models.CharField(max_length=255)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.version_name} ({self.version_number})"
