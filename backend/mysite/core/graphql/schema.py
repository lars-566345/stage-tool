import graphene
from .queries import Query
from .mutations import Mutation
from .mutations.login_mutation import LoginMutation

class CustomMutation(Mutation):
    login = LoginMutation.Field()

schema = graphene.Schema(query=Query, mutation=CustomMutation)
