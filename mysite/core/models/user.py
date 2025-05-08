from django.db import models


class User(models.Model):
    """
    Model representing a user.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024)
    is_student = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name