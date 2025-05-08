import graphene
from ..types.article_type import ArticleType
from ..types.user_type import UserType
from ...services.article_service import ArticleService

class GetAllArticles(graphene.ObjectType):
    articles = graphene.List(ArticleType)

    def resolve_articles(self, info):
        return ArticleService().get_all_articles()

class GetArticleById(graphene.ObjectType):
    article = graphene.Field(ArticleType, id=graphene.ID(required=True))

    def resolve_article(self, info, id):
        return ArticleService().get_article_by_id(id)