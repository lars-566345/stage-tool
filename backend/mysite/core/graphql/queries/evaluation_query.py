import graphene
from ..types.evaluation_type import EvaluationType
from ...services.evaluation_service import EvaluationService
import logging

logger = logging.getLogger(__name__)

class GetEvaluationsByStudentId(graphene.ObjectType):
    evaluations = graphene.List(EvaluationType, student_id=graphene.ID(required=True))

    def resolve_evaluations(self, info, student_id):
        return EvaluationService().get_evaluations_by_student_id(student_id)

class GetEvaluationById(graphene.ObjectType):
    evaluation = graphene.Field(EvaluationType, id=graphene.ID(required=True))

    def resolve_evaluation(self, info, id):
        return EvaluationService().get_evaluation_by_id(id)
    
class GetMyEvaluations(graphene.ObjectType):
    my_evaluations = graphene.List(EvaluationType)

    def resolve_my_evaluations(self, info):
        user = info.context.user
        if user.is_anonymous:
            return None
        if hasattr(user, 'student_profile'):
            return EvaluationService().get_evaluations_by_student_id(user.student_profile.id)
        return None