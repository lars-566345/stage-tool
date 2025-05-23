from ..models.phase import Phase
import logging

logger = logging.getLogger(__name__)

class PhaseRepository:
    def get_all_phases(self):
        try:
            phases = Phase.objects.all()
            logger.info("Retrieved all phases.")
            return phases
        except Phase.DoesNotExist:
            logger.warning("No phases found.")
            return None

    def get_phase_by_id(self, id: int):
        try:
            phase = Phase.objects.get(id=id)
            logger.info(f"Retrieved phase with id {id}.")
            return phase
        except Phase.DoesNotExist:
            logger.warning(f"Phase with id {id} does not exist.")
            return None

    def create_phase(self, phase: Phase):
        try:
            phase.save()
            logger.info(f"Created phase with id {phase.id}.")
            return phase
        except Exception as e:
            logger.error(f"Error creating phase: {e}")
            return e

    def update_phase(self, phase: Phase, content: str = None):
        try:
            if content is not None:
                phase.content = content
            phase.save()
            logger.info(f"Updated phase with id {phase.id}.")
            return True
        except Exception as e:
            logger.error(f"Error updating phase with id {phase.id}: {e}")
            return False

    def delete_phase(self, id: int):
        try:
            phase = self.get_phase_by_id(id)
            phase.delete()
            logger.info(f"Deleted phase with id {id}.")
            return True
        except Phase.DoesNotExist:
            logger.warning(f"Cannot delete phase with id {id}: does not exist.")
            return False