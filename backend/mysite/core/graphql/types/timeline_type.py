import graphene
from ...models.fix import Timeline
from graphene_django import DjangoObjectType
from .phase_type import PhaseType

class TimelineType(DjangoObjectType):
    class Meta:
        model = Timeline
        fields = "__all__"
