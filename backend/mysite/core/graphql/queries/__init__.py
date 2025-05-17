import graphene
from .article_query import GetAllArticles, GetArticleById
from .badge_query import GetAllBadges, GetBadgeById
from .evaluation_query import GetEvaluationsByStudentId, GetEvaluationById
from .phase_query import GetAllPhases, GetPhaseById
from .profile_query import GetProfileById, GetLoggedInUser

class Query(
    GetAllArticles, 
    GetArticleById, 
    
    GetAllBadges,
    GetBadgeById,

    GetEvaluationsByStudentId,
    GetEvaluationById,

    GetAllPhases,
    GetPhaseById,

    GetProfileById,
    GetLoggedInUser,
    
    graphene.ObjectType
):
    pass
