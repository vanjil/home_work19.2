from django.urls import path, include
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from .views import AnnouncementsListView, AnnouncementDetailView, AnnouncementCreateView, AnnouncementUpdateView, AnnouncementDeleteView, \
    HomeView, ContactView, AnnouncementViewSet, CategoryViewSet
from . import views
app_name = 'products'

router = DefaultRouter()
router.register(r'announcements', AnnouncementViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', AnnouncementsListView.as_view(), name='announcements_list'),
    path('<int:pk>/', cache_page(60)(AnnouncementDetailView.as_view()), name='announcement_detail'),
    path('create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement_delete'),
    path('home/', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('api/', include(router.urls)),
    path('announcements/', views.AnnouncementsListView.as_view(), name='announcement_list'),

]
