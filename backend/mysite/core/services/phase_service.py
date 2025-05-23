from ..repositories.phase_repository import *
import logging

logger = logging.getLogger(__name__)

class PhaseService:
    def __init__(self):
        self.phase_repository = PhaseRepository()

    def get_all_phases(self):
        logger.info("Fetching all phases")
        phases = self.phase_repository.get_all_phases()
        if not phases:
            logger.warning("No phases found")
            raise ValueError("No phases found")
        return phases

    def get_phase_by_id(self, id: int):
        logger.info(f"Fetching phase with id: {id}")
        phase = self.phase_repository.get_phase_by_id(id)
        if not phase:
            logger.warning(f"Phase with id {id} not found")
            raise ValueError("phase not found")
        return phase
    
    def create_phase(self, content: str):
        logger.info(f"Creating new phase with content: {content}")
        new_phase_instance = Phase(content=content)
        self.phase_repository.create_phase(new_phase_instance)
        logger.info("Phase created successfully")

    def update_phase(self, id: int, content: str = None):
        logger.info(f"Updating phase with id: {id}")
        phase_instance = self.phase_repository.get_phase_by_id(id)
        if not phase_instance:
            logger.warning(f"Phase with id {id} not found for update")
            raise ValueError("phase not found")
        self.phase_repository.update_phase(phase_instance, content)
        logger.info(f"Phase with id {id} updated successfully")

    def delete_phase(self, id: int):
        logger.info(f"Deleting phase with id: {id}")
        phase_instance = self.phase_repository.get_phase_by_id(id)
        if not phase_instance:
            logger.warning(f"Phase with id {id} not found for deletion")
            raise ValueError("phase not found")
        self.phase_repository.delete_phase(id)
        logger.info(f"Phase with id {id} deleted successfully")