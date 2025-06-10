import graphene
from ..types.student_profile_type import StudentProfileType
from ...services.student_profile_service import StudentProfileService
import logging

logger = logging.getLogger(__name__)

class GetStudentProfiles(graphene.ObjectType):
    student_profiles = graphene.List(StudentProfileType)

    def resolve_student_profiles(self, info):
        return StudentProfileService().get_all_profiles()

class GetStudentProfileById(graphene.ObjectType):
    student_profile = graphene.Field(StudentProfileType, id=graphene.ID(required=True))

    def resolve_student_profile(self, info, id):
        return StudentProfileService().get_profile_by_user_id(id)
    