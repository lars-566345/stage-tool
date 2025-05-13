import graphene
from ..types.phase_type import PhaseType
from ...services.phase_service import PhaseService

class CreatePhase(graphene.Mutation):
    class Arguments:
        content = graphene.String(required=True)

    phase = graphene.Field(PhaseType)

    def mutate(self, info, content):
        phase = PhaseService().create_phase(content)
        return CreatePhase(phase=phase)


class UpdatePhase(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        content = graphene.String()

    phase = graphene.Field(PhaseType)

    def mutate(self, info, id, content=None):
        phase = PhaseService().update_phase(id, content)
        return UpdatePhase(phase=phase)

## Not implemented in __init__.py
class DeletePhase(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        success = PhaseService().delete_phase(id)
        return DeletePhase(success=success)
