from ..repositories.user_repository import *

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_by_id(self, id: int):
        badge = self.user_repository.get_user_by_id(id)
        if not badge:
            raise ValueError("user not found")
        return badge
    
    def create_user(self, name: str, is_student: bool, is_admin: bool):
        new_user_instance = User(name=name, is_student=is_student, is_admin=is_admin)

        self.user_repository.create_user(new_user_instance)

    def update_user(self, name: str = None, is_student: bool = None, is_admin: bool = None):
        user_instance = self.user_repository.get_user_by_id(id)

        if not user_instance:
            raise ValueError("user not found")
        
        self.user_repository.update_user(user_instance, name, is_student, is_admin)


    def delete_user(self, id: int):
        user_instance = self.user_repository.get_user_by_id(id)

        if not user_instance:
            raise ValueError("user not found")
        
        self.user_repository.delete_user(id)