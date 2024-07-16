from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="adimin@exemplem.com")
        user.set_password("1234qwer")
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
