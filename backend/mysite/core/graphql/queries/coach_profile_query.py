import graphene
from ..types.coach_profile_type import CoachProfileType
from ...services.coach_profile_service import CoachProfileService

class GetCoachProfileById(graphene.ObjectType):
    coach_profile = graphene.Field(CoachProfileType, id=graphene.ID(required=True))

    def resolve_coach_profile(self, info, id):
        return CoachProfileService().get_profile_by_user_id(id)