import graphene
from ...models.fix import StudentDeliverableProgress
from graphene_django import DjangoObjectType

class StudentDeliverableProgressType(DjangoObjectType):
    deliverable_title = graphene.String()
    phase_title = graphene.String()

    class Meta:
        model = StudentDeliverableProgress
        fields = ('id', 'deliverable', 'phase', 'submitted', 'submitted_at')

    def resolve_deliverable_title(self, info):
        return self.deliverable.title if self.deliverable else None

    def resolve_phase_title(self, info):
        return self.phase.title if self.phase else None
