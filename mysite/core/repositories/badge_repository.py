from ..models.badge import Badge

class BadgeRepository:
    def get_all_badges(self):
        try:
            return Badge.objects.all()
        except Badge.DoesNotExist:
            return None

    def get_badge_by_id(self, id: int):
        try:
            return Badge.objects.get(id=id)
        except Badge.DoesNotExist:
            return None