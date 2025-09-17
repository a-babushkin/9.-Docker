from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для заполнения групп с настроенными правами"""

    def handle(self, *args, **options):
        # Создаем новую группу «Модераторы»
        moderators = Group.objects.create(name="Модераторы")

        # Создаем пользователя
        user = User.objects.create(email="moderators_1@mail.ru")
        user.set_password("12345")
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save()

        # Добавляем пользователя в группу «Менеджеры»
        user.groups.add(moderators)
