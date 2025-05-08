from ..repositories.evaluation_repository import *

class EvaluationService:
    def __init__(self):
        self.evaluation_repository = EvaluationRepository()

    def get_evaluations_by_student_id(self, student_id: int):
        evaluations = self.evaluation_repository.get_evaluations_by_student_id(student_id)
        if not evaluations:
            raise ValueError("No evaluations found")
        return evaluations

    def get_evaluation_by_id(self, id: int):
        evaluation = self.evaluation_repository.get_evaluation_by_id(id)
        if not evaluation:
            raise ValueError("evaluation not found")
        return evaluation
    