from ..models.user import User

class UserRepository:
    def get_user_by_id(self, id: int):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None