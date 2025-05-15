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