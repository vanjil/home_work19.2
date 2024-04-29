from django.db import models

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

    def __str__(self):
        return self.name
