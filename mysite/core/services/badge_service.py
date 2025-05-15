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
