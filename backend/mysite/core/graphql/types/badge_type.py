from ...models.fix import Badge
from graphene_django import DjangoObjectType

class BadgeType(DjangoObjectType):
    class Meta:
        model = Badge
        fields = ('id', 'label',)
        exclude_fields = ('students',)
