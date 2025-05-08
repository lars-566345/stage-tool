import graphene
from .article_query import GetAllArticles, GetArticleById
from .evaluation_query import GetEvaluationsByStudentId, GetEvaluationById

class Query(
    GetAllArticles, 
    GetArticleById, 
    
    GetEvaluationsByStudentId,
    GetEvaluationById,
    graphene.ObjectType
):
    pass
