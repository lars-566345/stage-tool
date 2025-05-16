from django.db import models
from .phase import Phase
from .article import Article


class ArticlePhase(models.Model):
    """
    Model representing a relationship between Badge and User
    """
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id)