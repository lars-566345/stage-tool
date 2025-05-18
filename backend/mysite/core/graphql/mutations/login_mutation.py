# myapp/graphql/mutations.py

import graphene
from django.contrib.auth import authenticate
from graphql_jwt.shortcuts import get_token

class LoginMutation(graphene.Mutation):
    token = graphene.String()
    success = graphene.Boolean()
    errors = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = authenticate(info.context, username=username, password=password)
        if not user:
            return LoginMutation(success=False, errors="Invalid credentials")

        token = get_token(user)
        info.context.jwt_cookie = token  # Save JWT token on request in cookie

        return LoginMutation(token=token, success=True, errors=None)
