from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

'''настройка автоматический документации'''
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('users/', include('users.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),#обслуживание мадиафайлов в режиме разработки
    path('blog/', include('blog.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # полученике JWT-токина
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #Обновление JWT-токена
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), #для просмотра и тестирования API
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),#для чистой и структурированной документации API.
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# временный код в режиме разработки, потом подключим например Nginx
