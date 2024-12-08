from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin_HW_curs6@mail.pro',
            first_name='Admin',
            last_name='HW_curs6',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('superuser_pass')
        user.save()
