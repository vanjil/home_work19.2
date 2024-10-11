from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField('Email', unique=True)

    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True, help_text='Введите номер')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', blank=True, null=True, help_text='Загрузите аватар')
    country = models.CharField(max_length=40, verbose_name='Страна', blank=True, null=True, help_text='Страна проживания')

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email