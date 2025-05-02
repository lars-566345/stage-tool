import graphene
from ..types.article_type import ArticleType
from ...services.article_service import ArticleService

class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType)

    def resolve_articles(self, info):
        return ArticleService().get_all_articles()

