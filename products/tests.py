from django.test import TestCase
from .models import Announcement, Category
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

class AnnouncementModelTest(TestCase):  # Переименован класс
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.user = User.objects.create_user(email='owner@example.com', password='password123')  # Создаем пользователя
        self.announcement = Announcement.objects.create(
            title='Test Announcement',
            description='Test Description',
            category=self.category,
            price=10.00,
            owner=self.user
        )

    def test_announcement_str(self):
        self.assertEqual(str(self.announcement), 'Test Announcement')

    def test_announcement_slug(self):
        self.assertEqual(self.announcement.slug, 'test-announcement')  # Предполагается, что slug формируется из title

class AnnouncementViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='password123')
        self.client.login(email='testuser@example.com', password='password123')
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.announcement = Announcement.objects.create(
            title='Test Announcement',
            description='Test Description',
            category=self.category,
            price=10.00,
            owner=self.user
        )

    def test_announcement_list_view(self):
        response = self.client.get(reverse('products:announcement_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Announcement')  # Проверка на наличие заголовка объявления

    def test_announcement_detail_view(self):
        response = self.client.get(reverse('products:announcement_detail', args=[self.announcement.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Announcement')  # Проверка на наличие заголовка объявления
