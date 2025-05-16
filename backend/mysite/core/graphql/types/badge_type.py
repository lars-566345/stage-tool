from graphene_django import DjangoObjectType
from ...models.badge import Badge

class BadgeType(DjangoObjectType):
    class Meta:
        model = Badge
        fields = "__all__"
