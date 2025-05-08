from graphene_django import DjangoObjectType
from ...models.evaluation import Evaluation

class EvaluationType(DjangoObjectType):
    class Meta:
        model = Evaluation
        fields = "__all__"
