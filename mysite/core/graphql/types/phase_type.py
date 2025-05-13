from graphene_django import DjangoObjectType
from ...models.phase import Phase

class PhaseType(DjangoObjectType):
    class Meta:
        model = Phase
        fields = "__all__"
