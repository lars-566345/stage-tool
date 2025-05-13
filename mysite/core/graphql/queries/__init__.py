import graphene
from .article_query import GetAllArticles, GetArticleById
from .badge_query import GetAllBadges, GetBadgeById
from .evaluation_query import GetEvaluationsByStudentId, GetEvaluationById
from .phase_query import GetAllPhases, GetPhaseById
from .user_query import GetUserById

class Query(
    GetAllArticles, 
    GetArticleById, 
    
    GetAllBadges,
    GetBadgeById,

    GetEvaluationsByStudentId,
    GetEvaluationById,

    GetAllPhases,
    GetPhaseById,

    GetUserById,
    
    graphene.ObjectType
):
    pass
