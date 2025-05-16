from ..repositories.evaluation_repository import *
from ..repositories.profile_repository import *
from ..repositories.phase_repository import *
from datetime import datetime, date

class EvaluationService:
    def __init__(self):
        self.evaluation_repository = EvaluationRepository()
        self.profile_repository = ProfileRepository()
        self.phase_repository = PhaseRepository()

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
    
    def create_evaluation(self, feedback: str, date: date, student: int, teacher: int, phase: int):
        student_instance = self.profile_repository.get_profile_by_user_id(student)
        teacher_instance = self.profile_repository.get_profile_by_user_id(teacher)
        phase_instance = self.phase_repository.get_phase_by_id(phase)

        if not student_instance:
            raise ValueError("Student not found")
        
        if not teacher_instance:
            raise ValueError("Teacher not found")
        
        if not phase_instance:
            raise ValueError("Phase not found")

        new_evaluation_instance = Evaluation(
            feedback=feedback,
            date=date,
            student=student_instance,
            teacher=teacher_instance,
            phase=phase_instance
            )

        self.evaluation_repository.create_evaluation(new_evaluation_instance)