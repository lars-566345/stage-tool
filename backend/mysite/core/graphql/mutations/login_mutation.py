import graphene
from django.contrib.auth import authenticate, login
from ..types.profile_type import ProfileType
from django.contrib.auth.models import User

class LoginMutation(graphene.Mutation):
    profile = graphene.Field(ProfileType)
    success = graphene.Boolean()
    errors = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        print(f"Mutate called with username={username}")
        request = info.context  # Django HttpRequest object
        user = authenticate(request, username=username, password=password)
        if user is None:
            return LoginMutation(success=False, errors="Invalid credentials")

        login(info.context, user)

        profile = getattr(user, "profile", None)
        return LoginMutation(success=True, profile=profile)
