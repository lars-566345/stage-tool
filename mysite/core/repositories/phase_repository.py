from ..models.phase import Phase

class PhaseRepository:
    def get_all_phases(self):
        try:
            return Phase.objects.all()
        except Phase.DoesNotExist:
            return None

    def get_phase_by_id(self, id: int):
        try:
            return Phase.objects.get(id=id)
        except Phase.DoesNotExist:
            return None
        

    def create_phase(self, phase: Phase):
        try:
            return phase.save()
        except Exception as e:
            return e

    def update_phase(self, phase: Phase, content: str = None):
        try:
            if content is not None:
                phase.content = content
            phase.save()
            return True
        except Exception as e:
            return False
            
    def delete_phase(self, id: int):
        try:
            phase = self.get_phase_by_id(id)
            phase.delete()
            return True
        except phase.DoesNotExist:
            return False