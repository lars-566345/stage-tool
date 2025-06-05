import graphene
from ...models.fix import StudentProfile
from graphene_django import DjangoObjectType
from .article_type import ArticleType
from .badge_type import BadgeType
from .student_phase_progress_type import StudentPhaseProgressType
from .student_deliverable_progress_type import StudentDeliverableProgressType
from .coach_profile_shallow_type import CoachProfileShallowType

class StudentProfileType(DjangoObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    coaches = graphene.List(CoachProfileShallowType)
    favorite_articles = graphene.List(ArticleType)
    earned_badges = graphene.List(BadgeType)
    phase_progress = graphene.List(StudentPhaseProgressType)
    deliverable_progress = graphene.List(StudentDeliverableProgressType)

    class Meta:
        model = StudentProfile
        fields = "__all__"
        exclude_fields = ('coaches',)

    def resolve_first_name(self, info):
        return self.user.first_name if self.user else None

    def resolve_last_name(self, info):
        return self.user.last_name if self.user else None
    
    def resolve_favorite_articles(self, info):
        return self.favorite_articles.all()
    
    def resolve_earned_badges(self, info):
        return self.earned_badges.all()
    
    def resolve_phase_progress(self, info):
        return self.phase_progress.all()
    
    def resolve_deliverable_progress(self, info):
        return self.deliverable_progress.all()
    
    def resolve_coaches(self, info):
        return [cs.coach for cs in self.student_coaches.all()]
