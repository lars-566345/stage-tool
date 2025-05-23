from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Sets up the test environment'

    def handle(self, *args, **options):
        self.stdout.write("Running migrations...")
        call_command('makemigrations', verbosity=1)
        call_command('migrate', verbosity=1)

        self.stdout.write("Setting up test data...")

        User = get_user_model()

        if not User.objects.filter(username='admin').exists():
            call_command('createsuperuser', interactive=False, username='admin', email='admin@example.com')
            user = User.objects.get(username='admin')
            user.set_password(os.getenv('DJANGO_SUPERUSER_PASSWORD'))
            user.save()
            self.stdout.write(self.style.SUCCESS("Superuser created."))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists."))

        
        if not User.objects.filter(username='teststudent').exists():
            test_user = User.objects.create_user(username='teststudent', first_name='Test', last_name='Student',)
            test_user.set_password("Hardware1!")
            test_user.save()
            self.stdout.write(self.style.SUCCESS("Test user created."))
        else:
            self.stdout.write(self.style.WARNING("Test user already exists."))

        if not User.objects.filter(username='testteacher').exists():
            test_user = User.objects.create_user(username='testteacher', first_name='Test', last_name='Teacher', is_student=False)
            test_user.set_password("Coaching1!")
            test_user.save()
            self.stdout.write(self.style.SUCCESS("Test user created."))
        else:
            self.stdout.write(self.style.WARNING("Test user already exists."))
        
        

        
        self.stdout.write(self.style.SUCCESS("Test environment setup complete."))
