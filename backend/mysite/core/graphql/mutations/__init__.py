import graphene
import graphql_jwt
from .article_mutation import CreateArticle, UpdateArticle, DeleteArticle
from .badge_mutation import CreateBadge, UpdateBadge, DeleteBadge
from .evaluation_mutation import CreateEvaluation
from .phase_mutation import CreatePhase, UpdatePhase, DeletePhase
from .login_mutation import LoginMutation
from graphql_jwt import ObtainJSONWebToken

class Mutation(graphene.ObjectType):
    login = LoginMutation.Field()

    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    create_article = CreateArticle.Field()
    update_article = UpdateArticle.Field()
    delete_article = DeleteArticle.Field()

    create_badge = CreateBadge.Field()
    update_badge = UpdateBadge.Field()
    delete_badge = DeleteBadge.Field()

    create_evaluation = CreateEvaluation.Field()

    create_phase = CreatePhase.Field()
    update_phase = UpdatePhase.Field()
    delete_phase = DeletePhase.Field()