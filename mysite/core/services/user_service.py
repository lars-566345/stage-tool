from ..repositories.user_repository import *

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_by_id(self, id: int):
        badge = self.user_repository.get_user_by_id(id)
        if not badge:
            raise ValueError("user not found")
        return badge
    