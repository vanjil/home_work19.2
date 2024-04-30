from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),  # добавляем маршрут для корневого URL-адреса
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]

# Добавляем правила для обработки медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
