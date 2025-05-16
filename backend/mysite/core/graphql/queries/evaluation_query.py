import graphene
from ..types.evaluation_type import EvaluationType
from ..types.user_type import UserType
from ...services.evaluation_service import EvaluationService

class GetEvaluationsByStudentId(graphene.ObjectType):
    evaluations = graphene.List(EvaluationType, student_id=graphene.ID(required=True))

    def resolve_evaluations(self, info, student_id):
        return EvaluationService().get_evaluations_by_student_id(student_id)

class GetEvaluationById(graphene.ObjectType):
    evaluation = graphene.Field(EvaluationType, id=graphene.ID(required=True))

    def resolve_evaluation(self, info, id):
        return EvaluationService().get_evaluation_by_id(id)