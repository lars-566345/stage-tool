from django.db import models
from .phase import Phase
from .profile import Profile


class Evaluation(models.Model):
    """
    Model representing a evaluation.
    """
    id = models.AutoField(primary_key=True)
    feedback = models.TextField()
    date = models.DateField()
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="student")
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="teacher")
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)