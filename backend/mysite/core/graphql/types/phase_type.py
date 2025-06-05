import graphene
from graphene_django import DjangoObjectType
from ...models.fix import Phase
from .deliverable_type import DeliverableType

class PhaseType(DjangoObjectType):
    class Meta:
        model = Phase
        fields = '__all__'