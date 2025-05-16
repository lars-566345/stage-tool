from ..repositories.badge_repository import *

class BadgeService:
    def __init__(self):
        self.badge_repository = BadgeRepository()

    def get_all_badges(self):
        badges = self.badge_repository.get_all_badges()
        if not badges:
            raise ValueError("No badges found")
        return badges

    def get_badge_by_id(self, id: int):
        badge = self.badge_repository.get_badge_by_id(id)
        if not badge:
            raise ValueError("badge not found")
        return badge

    def create_badge(self, title: str, description: str):
        new_badge_instance = Badge(title=title, description=description)

        self.badge_repository.create_badge(new_badge_instance)


    def update_badge(self, id: int, title: str = None, description: str = None):
        badge_instance = self.badge_repository.get_badge_by_id(id)

        if not badge_instance:
            raise ValueError("badge not found")
        
        self.badge_repository.update_badge(badge_instance, title, description)


    def delete_badge(self, id: int):
        badge_instance = self.badge_repository.get_badge_by_id(id)

        if not badge_instance:
            raise ValueError("badge not found")
        
        self.badge_repository.delete_badge(id)