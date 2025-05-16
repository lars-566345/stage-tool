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
    
    def create_phase(self, content: str):
        new_phase_instance = Phase(content=content)

        self.phase_repository.create_phase(new_phase_instance)

    def update_phase(self, id: int, content: str = None):
        phase_instance = self.phase_repository.get_phase_by_id(id)

        if not phase_instance:
            raise ValueError("phase not found")
        
        self.phase_repository.update_phase(phase_instance, content)


    def delete_phase(self, id: int):
        phase_instance = self.phase_repository.get_phase_by_id(id)

        if not phase_instance:
            raise ValueError("phase not found")
        
        self.phase_repository.delete_phase(id)