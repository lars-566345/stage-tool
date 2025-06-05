from graphene_django import DjangoObjectType
from ...models.fix import Deliverable

class DeliverableType(DjangoObjectType):
    class Meta:
        model = Deliverable
        fields = '__all__'