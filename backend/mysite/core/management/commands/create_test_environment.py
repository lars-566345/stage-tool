from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
import os
from core.models import *
from datetime import date

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
            user.set_password(os.getenv('DJANGO_SUPER_USER_PASSWORD'))
            user.save()
            self.stdout.write(self.style.SUCCESS("Superuser created."))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists."))

        
        if not User.objects.filter(username='teststudent').exists():
            test_student = User.objects.create_user(username='teststudent', first_name='Test', last_name='Student',)
            test_student.set_password("Hardware1!")
            test_student.save()
            self.stdout.write(self.style.SUCCESS("Test user created."))
        else:
            self.stdout.write(self.style.WARNING("Test user already exists."))

        if not User.objects.filter(username='testteacher').exists():
            test_teacher = User.objects.create_user(username='testteacher', first_name='Test', last_name='Teacher')
            test_teacher.set_password("Coaching1!")
            test_teacher.save()
            self.stdout.write(self.style.SUCCESS("Test user created."))
        else:
            self.stdout.write(self.style.WARNING("Test user already exists."))

        
        test_student_profile = Profile.objects.get(user=test_student)
        test_teacher_profile = Profile.objects.get(user=test_teacher)
        test_teacher_profile.is_student = False
        test_teacher_profile.save()


        test_phase = Phase.objects.create(content="Dit is fase 1")
        test_badge = Badge.objects.create(title="Kleintjes worden groot", description="Doe een eerste evaluatie")
        test_article = Article.objects.create(title="Hoe maak je een CV?", content="Dit is een test artikel", status=1, author=test_teacher_profile)
        test_evaluation = Evaluation.objects.create(feedback="Goed bezig!", date=date.today(), student=test_student_profile, teacher=test_teacher_profile, phase=test_phase)
        
        ProfileBadge.objects.create(earned_by=test_student_profile, given_by=test_teacher_profile, badge=test_badge)
        ArticlePhase.objects.create(article=test_article, phase=test_phase)
        TeacherStudent.objects.create(teacher=test_teacher_profile, student=test_student_profile)


        
        self.stdout.write(self.style.SUCCESS("Test environment setup complete."))
