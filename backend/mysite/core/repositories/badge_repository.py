from ..models.fix import Badge
import logging

logger = logging.getLogger(__name__)

class BadgeRepository:
    def get_all_badges(self):
        try:
            badges = Badge.objects.all()
            logger.info("Fetched all badges.")
            return badges
        except Badge.DoesNotExist:
            logger.warning("No badges found.")
            return None
        except Exception as e:
            logger.error(f"Error fetching all badges: {e}")
            return None

    def get_badge_by_id(self, id: int):
        try:
            badge = Badge.objects.get(id=id)
            logger.info(f"Fetched badge with id {id}.")
            return badge
        except Badge.DoesNotExist:
            logger.warning(f"Badge with id {id} does not exist.")
            return None
        except Exception as e:
            logger.error(f"Error fetching badge with id {id}: {e}")
            return None
        
    def create_badge(self, badge: Badge):
        try:
            badge.save()
            logger.info(f"Created badge with id {badge.id}.")
            return badge
        except Exception as e:
            logger.error(f"Error creating badge: {e}")
            return e
        
    def update_badge(self, badge: Badge, title: str = None, description: str = None):
        try:
            if title is not None:
                badge.title = title
            
            if description is not None:
                badge.description = description

            badge.save()
            logger.info(f"Updated badge with id {badge.id}.")
            return True
        except Exception as e:
            logger.error(f"Error updating badge with id {badge.id if badge else 'unknown'}: {e}")
            return False
            
    def delete_badge(self, id: int):
        try:
            badge = self.get_badge_by_id(id)
            badge.delete()
            logger.info(f"Deleted badge with id {id}.")
            return True
        except Badge.DoesNotExist:
            logger.warning(f"Cannot delete badge with id {id}: does not exist.")
            return False
        except Exception as e:
            logger.error(f"Error deleting badge with id {id}: {e}")
            return False
