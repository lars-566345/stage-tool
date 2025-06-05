from ..repositories.student_profile_repository import *
import logging

logger = logging.getLogger(__name__)

class StudentProfileService:
    def __init__(self):
        self.profile_repository = StudentProfileRepository()

    def get_all_profiles(self):
        logger.info(f"Fetching all student profiles")
        profiles = self.profile_repository.get_all_profiles()

        if not profiles:
            logger.warning(f"No profiles found")
            raise StudentProfile.DoesNotExist
        
        logger.debug(f"{len(profiles)} profiles found")
        return profiles

    def get_profile_by_user_id(self, id: int):
        logger.info(f"Fetching profile for user_id={id}")
        profile = self.profile_repository.get_profile_by_user_id(id)
    
        if not profile:
            logger.warning(f"No profile found for user_id={id}")
            raise StudentProfile.DoesNotExist
        
        logger.debug(f"Profile found for user_id={id}: {profile}")
        return profile