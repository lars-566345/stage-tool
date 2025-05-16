from ..repositories.profile_repository import *

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def get_profile_by_user_id(self, id: int):
        profile = self.profile_repository.get_profile_by_user_id(id)
    
        if not profile:
            raise Profile.DoesNotExist
        
        print(profile)
        
        return profile