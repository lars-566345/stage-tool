import graphene
from ..types.phase_type import PhaseType
from ...services.phase_service import PhaseService

class GetAllPhases(graphene.ObjectType):
    phases = graphene.List(PhaseType)

    def resolve_phases(self, info):
        return PhaseService().get_all_phases()

class GetPhaseById(graphene.ObjectType):
    phase = graphene.Field(PhaseType, id=graphene.ID(required=True))

    def resolve_phase(self, info, id):
        return PhaseService().get_phase_by_id(id)