from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Создание группы модераторов с необходимыми разрешениями'

    def handle(self, *args, **kwargs):
        # Создание или получение группы "Moderators"
        moderators, created = Group.objects.get_or_create(name='Moderators')

        # Поиск существующих разрешений и добавление их в группу
        permissions = [
            Permission.objects.get(id=49),  # can_unpublish_product
            Permission.objects.get(id=50),  # can_change_any_description
            Permission.objects.get(id=51)   # can_change_any_category
        ]

        for perm in permissions:
            moderators.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Группа модераторов успешно создана и разрешения добавлены'))
