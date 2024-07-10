from django.contrib.auth.forms import UserCreationForm

from products.forms import CrispyFormMixin
from users.models import User


class UserRegisterForm(CrispyFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

