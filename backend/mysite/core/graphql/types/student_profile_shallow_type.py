import graphene
from ...models.fix import StudentProfile
from graphene_django import DjangoObjectType

class StudentProfileShallowType(DjangoObjectType):
    first_name = graphene.String()
    last_name = graphene.String()

    class Meta:
        model = StudentProfile
        fields = ('id',)
        exclude_fields = ('coaches',)

    def resolve_first_name(self, info):
        return self.user.first_name if self.user else None
    
    def resolve_last_name(self, info):
        return self.user.last_name if self.user else None