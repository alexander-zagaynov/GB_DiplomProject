from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Alexander', email='alexander.zagaynov@gmail.com', password='secret', age=44)

        user.save()
        self.stdout.write(f'{user}')