from ..models.evaluation import Evaluation
import logging

logger = logging.getLogger(__name__)

class EvaluationRepository:
    def get_evaluations_by_student_id(self, student_id: int):
        try:
            evaluations = Evaluation.objects.filter(student=student_id)
            logger.info(f"Retrieved evaluations for student_id={student_id}")
            return evaluations
        except Evaluation.DoesNotExist:
            logger.warning(f"No evaluations found for student_id={student_id}")
            return None
        except Exception as e:
            logger.error(f"Error retrieving evaluations for student_id={student_id}: {e}")
            return None

    def get_evaluation_by_id(self, id: int):
        try:
            evaluation = Evaluation.objects.get(id=id)
            logger.info(f"Retrieved evaluation with id={id}")
            return evaluation
        except Evaluation.DoesNotExist:
            logger.warning(f"Evaluation with id={id} does not exist")
            return None
        except Exception as e:
            logger.error(f"Error retrieving evaluation with id={id}: {e}")
            return None
        
    def create_evaluation(self, evaluation: Evaluation):
        try:
            evaluation.save()
            logger.info(f"Created evaluation with id={evaluation.id}")
            return evaluation
        except Exception as e:
            logger.error(f"Error creating evaluation: {e}")
            return e