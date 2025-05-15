from ..repositories.phase_repository import *

class PhaseService:
    def __init__(self):
        self.phase_repository = PhaseRepository()

    def get_all_phases(self):
        phases = self.phase_repository.get_all_phases()
        if not phases:
            raise ValueError("No phases found")
        return phases

    def get_phase_by_id(self, id: int):
        badge = self.phase_repository.get_phase_by_id(id)
        if not badge:
            raise ValueError("phase not found")
        return badge
    