from django.db import models


class Phase(models.Model):
    """
    Model representing a phase.
    """
    id = models.AutoField(primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.id