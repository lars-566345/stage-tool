import graphene
from ..types.profile_type import ProfileType
from ...services.profile_service import ProfileService

class GetProfileById(graphene.ObjectType):
    profile = graphene.Field(ProfileType, id=graphene.ID(required=True))

    def resolve_profile(self, info, id):
        return ProfileService().get_profile_by_user_id(id)
    
## class GetAssignedStudents(graphene.ObjectType):
## class GetAssignedMentor(graphene.ObjectType):
## make sure student -> mentor is one to many in userproperty