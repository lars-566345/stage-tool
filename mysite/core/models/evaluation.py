from django.db import models
from .user import User
from .phase import Phase


class Evaluation(models.Model):
    """
    Model representing a evaluation.
    """
    id = models.AutoField(primary_key=True)
    feedback = models.TextField()
    date = models.DateTimeField()
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher")
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)


    def __str__(self):
        return self.id