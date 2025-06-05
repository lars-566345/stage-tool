import graphene
from .article_query import GetAllArticles, GetArticleById
from .badge_query import GetAllBadges, GetBadgeById
from .evaluation_query import GetEvaluationsByStudentId, GetEvaluationById, GetMyEvaluations
from .student_profile_query import GetStudentProfileById, GetStudentProfiles
from .coach_profile_query import GetCoachProfileById
from .profile_query import GetLoggedInUser

class Query(
    GetAllArticles, 
    GetArticleById, 
    
    GetAllBadges,
    GetBadgeById,

    GetEvaluationsByStudentId,
    GetEvaluationById,
    GetMyEvaluations,

    GetStudentProfiles,
    GetStudentProfileById,
    
    GetCoachProfileById,
    GetLoggedInUser,
    
    graphene.ObjectType
):
    pass
