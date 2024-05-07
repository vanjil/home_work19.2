from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='blog_post_list'),
    path('<int:pk>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('admin/', admin.site.urls),  # Добавляем маршрут для административной панели Django
    path('', include('products.urls')),  # добавляем маршрут для корневого URL-адреса
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),  # Добавляем маршрут для
    # обслуживания медиафайлов
]

