from ..models.evaluation import Evaluation

class EvaluationRepository:
    def get_evaluations_by_student_id(self, student_id: int):
        try:
            return Evaluation.objects.filter(student=student_id)
        except Evaluation.DoesNotExist:
            return None

    def get_evaluation_by_id(self, id: int):
        try:
            return Evaluation.objects.get(id=id)
        except Evaluation.DoesNotExist:
            return None
        
    def create_evaluation(self, evaluation: Evaluation):
        try:
            return evaluation.save()
        except Exception as e:
            return e