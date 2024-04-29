from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from products.views import (ProductsListView, ProductsDetailView, ProductsCreateView,
                            ProductsUpdateView, ProductsDeleteView)

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='products_detail'),
    path('admin/', admin.site.urls),
    path('products/create/', ProductsCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', ProductsUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', ProductsDeleteView.as_view(), name='products_delete'),
    path('products/', include('products.urls')),  # Подключаем URL-адреса приложения products
]

# Добавляем правила для обработки медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
