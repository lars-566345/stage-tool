import logging
from ..repositories.badge_repository import *

logger = logging.getLogger(__name__)

class BadgeService:
    def __init__(self):
        self.badge_repository = BadgeRepository()

    def get_all_badges(self):
        logger.info("Fetching all badges")
        badges = self.badge_repository.get_all_badges()
        if not badges:
            logger.warning("No badges found")
            raise ValueError("No badges found")
        logger.debug(f"Found {len(badges)} badges")
        return badges

    def get_badge_by_id(self, id: int):
        logger.info(f"Fetching badge with id={id}")
        badge = self.badge_repository.get_badge_by_id(id)
        if not badge:
            logger.warning(f"Badge with id={id} not found")
            raise ValueError("badge not found")
        logger.debug(f"Found badge: {badge}")
        return badge

    def create_badge(self, title: str, description: str):
        logger.info(f"Creating badge with title='{title}'")
        new_badge_instance = Badge(title=title, description=description)
        self.badge_repository.create_badge(new_badge_instance)
        logger.debug(f"Badge created: {new_badge_instance}")

    def update_badge(self, id: int, title: str = None, description: str = None):
        logger.info(f"Updating badge with id={id}")
        badge_instance = self.badge_repository.get_badge_by_id(id)
        if not badge_instance:
            logger.warning(f"Badge with id={id} not found for update")
            raise ValueError("badge not found")
        self.badge_repository.update_badge(badge_instance, title, description)
        logger.debug(f"Badge updated: id={id}, title={title}, description={description}")

    def delete_badge(self, id: int):
        logger.info(f"Deleting badge with id={id}")
        badge_instance = self.badge_repository.get_badge_by_id(id)
        if not badge_instance:
            logger.warning(f"Badge with id={id} not found for deletion")
            raise ValueError("badge not found")
        self.badge_repository.delete_badge(id)
        logger.debug(f"Badge deleted: id={id}")