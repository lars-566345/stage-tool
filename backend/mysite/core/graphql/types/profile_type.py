import graphene
from graphene_django import DjangoObjectType
from ...models.profile import Profile

class ProfileType(DjangoObjectType):
    first_name = graphene.String()
    last_name = graphene.String()

    class Meta:
        model = Profile
        fields = "__all__"

    def resolve_first_name(self, info):
        return self.user.first_name if self.user else None

    def resolve_last_name(self, info):
        return self.user.last_name if self.user else None
