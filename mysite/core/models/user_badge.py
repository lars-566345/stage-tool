from django.db import models
from .user import User
from .badge import Badge


class UserBadge(models.Model):
    """
    Model representing a relationship between Badge and User
    """
    id = models.AutoField(primary_key=True)
    earned_on = models.DateTimeField(auto_now_add=True)
    earned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="earned_by")
    given_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="given_by")
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)


    def __str__(self):
        return self.id