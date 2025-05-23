import logging
from ..repositories.evaluation_repository import *
from ..repositories.profile_repository import *
from ..repositories.phase_repository import *
from datetime import datetime, date

logger = logging.getLogger(__name__)

class EvaluationService:
    def __init__(self):
        self.evaluation_repository = EvaluationRepository()
        self.profile_repository = ProfileRepository()
        self.phase_repository = PhaseRepository()

    def get_evaluations_by_student_id(self, student_id: int):
        logger.info(f"Fetching evaluations for student_id={student_id}")
        evaluations = self.evaluation_repository.get_evaluations_by_student_id(student_id)
        if not evaluations:
            logger.warning(f"No evaluations found for student_id={student_id}")
            raise ValueError("No evaluations found")
        logger.debug(f"Found {len(evaluations)} evaluations for student_id={student_id}")
        return evaluations

    def get_evaluation_by_id(self, id: int):
        logger.info(f"Fetching evaluation by id={id}")
        evaluation = self.evaluation_repository.get_evaluation_by_id(id)
        if not evaluation:
            logger.warning(f"Evaluation not found for id={id}")
            raise ValueError("evaluation not found")
        logger.debug(f"Found evaluation: {evaluation}")
        return evaluation
    
    def create_evaluation(self, feedback: str, date: date, student: int, teacher: int, phase: int):
        logger.info(f"Creating evaluation for student={student}, teacher={teacher}, phase={phase}")
        student_instance = self.profile_repository.get_profile_by_user_id(student)
        teacher_instance = self.profile_repository.get_profile_by_user_id(teacher)
        phase_instance = self.phase_repository.get_phase_by_id(phase)

        if not student_instance:
            logger.error(f"Student not found: {student}")
            raise ValueError("Student not found")
        
        if not teacher_instance:
            logger.error(f"Teacher not found: {teacher}")
            raise ValueError("Teacher not found")
        
        if not phase_instance:
            logger.error(f"Phase not found: {phase}")
            raise ValueError("Phase not found")

        new_evaluation_instance = Evaluation(
            feedback=feedback,
            date=date,
            student=student_instance,
            teacher=teacher_instance,
            phase=phase_instance
        )

        self.evaluation_repository.create_evaluation(new_evaluation_instance)
        logger.info(f"Evaluation created successfully for student={student}, teacher={teacher}, phase={phase}")