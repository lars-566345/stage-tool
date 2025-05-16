import graphene
from ..types.evaluation_type import EvaluationType
from ...services.evaluation_service import EvaluationService

class CreateEvaluation(graphene.Mutation):
    class Arguments:
        feedback = graphene.String(required=True)
        date = graphene.Date(required=False)
        student = graphene.Int(required=True)
        teacher = graphene.Int(required=True)
        phase = graphene.Int(required=True)

    evaluation = graphene.Field(EvaluationType)

    def mutate(self, info, feedback, date, student, teacher, phase):
        evaluation = EvaluationService().create_evaluation(feedback, date, student, teacher, phase)
        return CreateEvaluation(evaluation=evaluation)
