import logging
from ..models.fix import CoachProfile

logger = logging.getLogger(__name__)

class CoachProfileRepository:
    def get_profile_by_user_id(self, id: int):
        try:
            profile = CoachProfile.objects.select_related('user').get(id=id)
            logger.info(f"Profile retrieved for user id {id}")
            return profile
        except CoachProfile.DoesNotExist:
            logger.warning(f"No profile found for user id {id}")
            return None
        except Exception as e:
            logger.error(f"Error retrieving profile for user id {id}: {e}")
            return None