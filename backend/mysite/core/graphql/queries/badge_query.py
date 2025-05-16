import graphene
from ..types.badge_type import BadgeType
from ...services.badge_service import BadgeService

class GetAllBadges(graphene.ObjectType):
    badges = graphene.List(BadgeType)

    def resolve_badges(self, info):
        return BadgeService().get_all_badges()

class GetBadgeById(graphene.ObjectType):
    badge = graphene.Field(BadgeType, id=graphene.ID(required=True))

    def resolve_badge(self, info, id):
        return BadgeService().get_badge_by_id(id)