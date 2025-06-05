from ...models.fix import KnowledgeBaseArticle
from graphene_django import DjangoObjectType

class ArticleType(DjangoObjectType):
    class Meta:
        model = KnowledgeBaseArticle
        fields = ('id', 'tag', 'title', 'content', 'created_at')
        exclude_fields = ('favorited_by',)
