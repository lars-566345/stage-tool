from graphene_django import DjangoObjectType
from ...models.user import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
