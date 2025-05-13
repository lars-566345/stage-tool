import graphene
from .article_mutation import CreateArticle, UpdateArticle
from .badge_mutation import CreateBadge, UpdateBadge
from .evaluation_mutation import CreateEvaluation
from .phase_mutation import CreatePhase, UpdatePhase
from .user_mutation import CreateUser, UpdateUser

class Mutation(graphene.ObjectType):
    create_article = CreateArticle.Field()
    update_article = UpdateArticle.Field()

    create_badge = CreateBadge.Field()
    update_badge = UpdateBadge.Field()

    create_evaluation = CreateEvaluation.Field()

    create_phase = CreatePhase.Field()
    update_phase = UpdatePhase.Field()

    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()


