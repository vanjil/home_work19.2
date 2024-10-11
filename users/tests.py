from django.test import TestCase
from products.models import Announcement, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class AnnouncementAPITest(TestCase):
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
