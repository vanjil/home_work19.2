from django.urls import path
from products import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<int:pk>/', views.products_detail, name='products_detail'),
    path('admin/', admin.site.urls),
]

# Добавляем правила для обработки медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
