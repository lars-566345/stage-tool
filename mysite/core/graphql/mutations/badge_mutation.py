import graphene
from ..types.badge_type import BadgeType
from ...services.badge_service import BadgeService

class CreateBadge(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=False)

    badge = graphene.Field(BadgeType)

    def mutate(self, info, title, description):
        badge = BadgeService().create_badge(title, description)
        return CreateBadge(badge=badge)


class UpdateBadge(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()

    badge = graphene.Field(BadgeType)

    def mutate(self, info, id, title=None, description=None):
        badge = BadgeService().update_badge(id, title, description)
        return UpdateBadge(badge=badge)

## Not implemented in __init__.py
class DeleteBadge(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        success = BadgeService().delete_badge(id)
        return DeleteBadge(success=success)
