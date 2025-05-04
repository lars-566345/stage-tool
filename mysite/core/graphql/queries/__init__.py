import graphene
from .article_query import GetAllArticles, GetArticleById

class Query(
    GetAllArticles, 
    GetArticleById, 
    graphene.ObjectType
):
    pass
