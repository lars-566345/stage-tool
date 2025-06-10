import graphene
from ..types.student_profile_type import StudentProfileType
from ..types.coach_profile_type import CoachProfileType 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class UserProfileUnion(graphene.Union):
    class Meta:
        types = (StudentProfileType, CoachProfileType)
        
class GetLoggedInUser(graphene.ObjectType):
    me = graphene.Field(UserProfileUnion)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            return None
        if hasattr(user, 'student_profile'):
            return user.student_profile
        elif hasattr(user, 'coach_profile'):
            return user.coach_profile
        return None    
    