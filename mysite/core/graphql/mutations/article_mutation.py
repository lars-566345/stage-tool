import graphene
from ..types.article_type import ArticleType
from ...services.article_service import ArticleService

class CreateArticle(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=False)
        status = graphene.Int(required=True)
        author = graphene.Int(required=True)

    article = graphene.Field(ArticleType)

    def mutate(self, info, title, content, status, author):
        article = ArticleService().create_article(title, content, status, author)
        return CreateArticle(article=article)


class UpdateArticle(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        content = graphene.String()
        status = graphene.Int()

    article = graphene.Field(ArticleType)

    def mutate(self, info, id, title=None, content=None, status=None):
        article = ArticleService().update_article(id, title, content, status)
        return UpdateArticle(article=article)

## Not implemented in __init__.py
class DeleteArticle(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        success = ArticleService().delete_article(id)
        return DeleteArticle(success=success)
