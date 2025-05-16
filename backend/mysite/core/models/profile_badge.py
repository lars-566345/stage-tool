from django.db import models
from .badge import Badge
from .profile import Profile


class ProfileBadge(models.Model):
    """
    Model representing a relationship between Badge and User
    """
    id = models.AutoField(primary_key=True)
    earned_on = models.DateTimeField(auto_now_add=True)
    earned_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="earned_by")
    given_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="given_by")
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)


    def __str__(self):
        return f"{str(self.earned_by.user.first_name)} - {self.badge.title}"