from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")  # Категория
    year = models.IntegerField(null=True, blank=True, verbose_name="Год выпуска")  # Добавлено поле для года выпуска
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Цена")  # Цена (опционально)
    location = models.CharField(max_length=100, null=True, blank=True, verbose_name="Местоположение")  # Местоположение
    contact_info = models.CharField(max_length=100, null=True, blank=True, verbose_name="Контактная Информация")  # Контактная информация
    photo = models.ImageField(upload_to='announcement_photos', default='default_photo.jpg', verbose_name="Добавить фото")  # Фотография
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcements', null=True, verbose_name="Владелец")  # Владелец
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления
    views_counter = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')  # Счетчик просмотров
    published = models.BooleanField(default=True)  # Статус публикации
    slug = models.SlugField(unique=True, blank=True)  # Слаг для URL
    published_at = models.DateTimeField(default=timezone.now)  # Дата публикации

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Создание слага на основе заголовка
            i = 1
            while Announcement.objects.filter(slug=self.slug).exists():  # Проверка уникальности
                self.slug = slugify(f"{self.title}-{i}")
                i += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_unpublish_announcement", "Can unpublish announcement"),
            ("can_change_any_description", "Can change any description"),
            ("can_change_any_category", "Can change any category"),
        ]

class Version(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='versions', on_delete=models.CASCADE, default=1)
    version_number = models.CharField(max_length=50)
    version_name = models.CharField(max_length=255)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.version_name} ({self.version_number})"