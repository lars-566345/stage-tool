import graphene
from ...models.fix import Evaluation
from graphene_django import DjangoObjectType

class EvaluationType(DjangoObjectType):
    student_name = graphene.String()
    coach_name = graphene.String()

    class Meta:
        model = Evaluation
        fields = ('id', 'feedback', 'created_at')

    def resolve_student_name(self, info):
        return self.student.user.get_full_name() if self.student and self.student.user else None
    
    def resolve_coach_name(self, info):
        return self.coach.user.get_full_name() if self.coach and self.coach.user else None
