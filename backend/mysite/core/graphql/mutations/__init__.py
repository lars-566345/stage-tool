import graphene
import graphql_jwt
from .login_mutation import LoginMutation
from graphql_jwt import ObtainJSONWebToken

class Mutation(graphene.ObjectType):
    login = LoginMutation.Field()

    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()