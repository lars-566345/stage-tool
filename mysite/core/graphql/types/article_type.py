from graphene_django import DjangoObjectType
from ...models.article import Article

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = "__all__"
