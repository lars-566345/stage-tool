import logging
from ..models.fix import StudentProfile

logger = logging.getLogger(__name__)

class StudentProfileRepository:
    def get_all_profiles(self):
        try:
            profiles = StudentProfile.objects.all()
            logger.info(f"{len(profiles)} profiles found")
            return profiles
        except StudentProfile.DoesNotExist:
            logger.exception("An error occurred getting all Student Profiles. No student profiles exist!")
            return None

    def get_profile_by_user_id(self, id: int):
        try:
            profile = StudentProfile.objects.select_related('user').get(id=id)
            logger.info(f"Profile retrieved for user id {id}")
            return profile
        except StudentProfile.DoesNotExist:
            logger.warning(f"No profile found for user id {id}")
            return None
        except Exception as e:
            logger.error(f"Error retrieving profile for user id {id}: {e}")
            return None