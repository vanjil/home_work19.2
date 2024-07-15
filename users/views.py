import secrets
import random
import string

from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views import View

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.form import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class PasswordResetView(View):
    def get(self, request):
        return render(request, 'password_reset.html')

    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.password = make_password(new_password)
            user.save()
            send_mail(
                subject="Восстановление пароля",
                message=f"Ваш новый пароль: {new_password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
            )
            return redirect(reverse('users:login'))
        return render(request, 'password_reset.html', {'error': 'Пользователь с таким email не найден.'})