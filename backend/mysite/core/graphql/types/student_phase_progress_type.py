import graphene
from ...models.fix import StudentPhaseProgress
from graphene_django import DjangoObjectType

class StudentPhaseProgressType(DjangoObjectType):
    phase_title = graphene.String()

    class Meta:
        model = StudentPhaseProgress
        fields = ('id', 'phase', 'status', 'updated_at')

    def resolve_phase_title(self, info):
        return self.phase.title if self.phase else None
