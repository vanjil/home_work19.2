from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from django.urls import path, include

from users.views import UserCreateView, email_verification, PasswordResetView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

app_name = UsersConfig.name
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm '),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/', include(router.urls)),

]
