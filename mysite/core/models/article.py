from django.db import models
from .profile import Profile


class Article(models.Model):
    """
    Model representing a article.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1024)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField()
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title