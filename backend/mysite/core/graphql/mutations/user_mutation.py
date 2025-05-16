import graphene
from ..types.user_type import UserType
from ...services.user_service import UserService

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        is_student = graphene.Boolean(required=True)
        is_admin = graphene.Boolean(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, name, is_student, is_admin):
        user = UserService().create_user(name, is_student, is_admin)
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        is_student = graphene.Boolean(required=True)
        is_admin = graphene.Boolean(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, id, name=None, is_student=None, is_admin=None):
        user = UserService().update_user(id, name, is_student, is_admin)
        return UpdateUser(user=user)

## Not implemented in __init__.py
class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        success = UserService().delete_user(id)
        return DeleteUser(success=success)
