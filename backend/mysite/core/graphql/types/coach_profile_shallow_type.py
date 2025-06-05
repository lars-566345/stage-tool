import graphene
from ...models.fix import CoachProfile
from graphene_django import DjangoObjectType

class CoachProfileShallowType(DjangoObjectType):
    first_name = graphene.String()
    last_name = graphene.String()

    class Meta:
        model = CoachProfile
        fields = ('id', 'first_name', 'last_name')
        exclude_fields = ('coach_students', 'students')

    def resolve_first_name(self, info):
        return self.user.first_name if self.user else None

    def resolve_last_name(self, info):
        return self.user.last_name if self.user else None