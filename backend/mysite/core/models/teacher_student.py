from django.db import models
from .profile import Profile


class TeacherStudent(models.Model):
    """
    Model representing a evaluation.
    """
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="pupil")
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="coach")


    def __str__(self):
        return f"{self.teacher} - {self.student}"