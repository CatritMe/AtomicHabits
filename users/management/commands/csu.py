from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='11111@11111.com')
        user.set_password('11111')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.save()
