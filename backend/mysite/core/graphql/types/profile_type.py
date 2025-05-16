from graphene_django import DjangoObjectType
from ...models.profile import Profile

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"
        # Not the password :)
