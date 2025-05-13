import graphene
from ..types.user_type import UserType
from ...services.user_service import UserService

class GetUserById(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.ID(required=True))

    def resolve_user(self, info, id):
        return UserService().get_user_by_id(id)
    
## class GetAssignedStudents(graphene.ObjectType):
## class GetAssignedMentor(graphene.ObjectType):
## make sure student -> mentor is one to many in userproperty