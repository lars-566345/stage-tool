from ..models.user import User

class UserRepository:
    def get_user_by_id(self, id: int):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
        

    def create_user(self, user: User):
        try:
            return user.save()
        except Exception as e:
            return e

    def update_user(self, user: User, name: str = None, is_student: bool = None, is_admin: bool = None):
        try:
            if name is not None:
                user.name = name
            
            if is_student is not None:
                user.is_student = is_student
            
            if is_admin is not None:
                user.is_admin = is_admin

            user.save()
            return True
        except Exception as e:
            return False
            
    def delete_user(self, id: int):
        try:
            user = self.get_user_by_id(id)
            user.delete()
            return True
        except User.DoesNotExist:
            return False