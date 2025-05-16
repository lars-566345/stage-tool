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
        
    def create_badge(self, badge: Badge):
        try:
            return badge.save()
        except Exception as e:
            return e
        
    def update_badge(self, badge: Badge, title: str = None, description: str = None):
        try:
            if title is not None:
                badge.title = title
            
            if description is not None:
                badge.description = description

            badge.save()
            return True
        except Exception as e:
            return False
            
    def delete_badge(self, id: int):
        try:
            badge = self.get_badge_by_id(id)
            badge.delete()
            return True
        except Badge.DoesNotExist:
            return False
