from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Announcement
from django.contrib.auth import get_user_model

User = get_user_model()

class AnnouncementAPITest(APITestCase):
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

    def test_announcement_list_api(self):
        response = self.client.get('/api/announcements/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_announcement_detail_api(self):
        response = self.client.get(f'/api/announcements/{self.announcement.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Announcement')

    def test_create_announcement_api(self):
        response = self.client.post('/api/announcements/', {
            'title': 'New Announcement',
            'description': 'New Description',
            'category': self.category.id,
            'price': 15.00,
            'location': 'Test Location',
            'contact_info': 'test@example.com',
            'photo': '',  # Здесь можно добавить файл изображения, если требуется
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Announcement.objects.count(), 2)  # Проверяем, что объявление добавилось

    def test_update_announcement_api(self):
        response = self.client.put(f'/api/announcements/{self.announcement.id}/', {
            'title': 'Updated Announcement',
            'description': 'Updated Description',
            'category': self.category.id,
            'price': 20.00,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.announcement.refresh_from_db()  # Обновляем объект из базы данных
        self.assertEqual(self.announcement.title, 'Updated Announcement')

    def test_delete_announcement_api(self):
        response = self.client.delete(f'/api/announcements/{self.announcement.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Announcement.objects.count(), 0)  # Проверяем, что объявление было удалено
