import graphene
from ...models.fix import CoachProfile
from graphene_django import DjangoObjectType
from .student_profile_type import StudentProfileType

class CoachProfileType(DjangoObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    assigned_students = graphene.List(StudentProfileType)

    class Meta:
        model = CoachProfile
        fields = ('id', 'first_name', 'last_name', 'assigned_students')
        exclude_fields = ('coach_students', 'students')

    def resolve_first_name(self, info):
        return self.user.first_name if self.user else None

    def resolve_last_name(self, info):
        return self.user.last_name if self.user else None
    
    def resolve_assigned_students(self, info):
        return [cs.student for cs in self.coach_students.all()]