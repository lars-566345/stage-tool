from ..models.profile import Profile

class ProfileRepository:
    def get_profile_by_user_id(self, id: int):
        try:
            return Profile.objects.select_related('user').get(id=id)
        except Profile.DoesNotExist:
            return None