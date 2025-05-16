from django.db import models


class Badge(models.Model):
    """
    Model representing a badge.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.title