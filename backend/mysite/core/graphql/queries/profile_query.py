import graphene
from ..types.profile_type import ProfileType
from ...services.profile_service import ProfileService
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class GetProfileById(graphene.ObjectType):
    profile = graphene.Field(ProfileType, id=graphene.ID(required=True))

    def resolve_profile(self, info, id):
        return ProfileService().get_profile_by_user_id(id)
    
class GetLoggedInUser(graphene.ObjectType):
    me = graphene.Field(ProfileType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            return None
        return getattr(user, 'profile', None)    
    
## class GetAssignedStudents(graphene.ObjectType):
## class GetAssignedMentor(graphene.ObjectType):
## make sure student -> mentor is one to many in userproperty