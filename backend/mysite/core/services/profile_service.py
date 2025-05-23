from ..repositories.profile_repository import *
import logging

logger = logging.getLogger(__name__)

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def get_profile_by_user_id(self, id: int):
        logger.info(f"Fetching profile for user_id={id}")
        profile = self.profile_repository.get_profile_by_user_id(id)
    
        if not profile:
            logger.warning(f"No profile found for user_id={id}")
            raise Profile.DoesNotExist
        
        logger.debug(f"Profile found for user_id={id}: {profile}")
        return profile