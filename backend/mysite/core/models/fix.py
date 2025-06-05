from django.contrib.auth.models import User
from django.db import models

class KnowledgeBaseArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tag = models.CharField(max_length=56)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Deliverable(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Phase(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField()
    deliverables = models.ManyToManyField(Deliverable, related_name='phases')
    identity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.order}: {self.title}"
    
class Timeline(models.Model):
    phases = models.ManyToManyField(Phase, related_name='timelines')

    def __str__(self):
        return "default timeline"

class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='coach_profile')
    students = models.ManyToManyField('StudentProfile', through='CoachStudent', related_name='coaches')

    def __str__(self):
        if self.user:
            return f"Coach({self.user.first_name})"
        else:
            return "CoachProfile with no user"
        

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='student_profile')
    timeline = models.ForeignKey(Timeline, on_delete=models.SET_NULL, null=True, blank=True)
    favorite_articles = models.ManyToManyField(KnowledgeBaseArticle, blank=True, related_name='favorited_by')
    earned_badges = models.ManyToManyField('Badge', through='StudentBadge', related_name='students')

    def __str__(self):
        if self.user:
            return f"Student({self.user.first_name} {self.user.last_name})"
        else:
            return "StudentProfile with no user"
        
class CoachStudent(models.Model):
    coach = models.ForeignKey('CoachProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name='coach_students')
    student = models.ForeignKey('StudentProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name='student_coaches')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('coach', 'student')

    def __str__(self):
        return f"{self.coach} - {self.student}"
    
class StudentPhaseProgress(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='phase_progress')
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'phase')

    def __str__(self):
        return f"{self.student.__str__} - {self.phase.title}: {self.status}"
    
class StudentDeliverableProgress(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='deliverable_progress')
    deliverable = models.ForeignKey(Deliverable, on_delete=models.CASCADE)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    submitted = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'deliverable', 'phase')
    
class Evaluation(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='evaluations')
    coach = models.ForeignKey(CoachProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='given_feedbacks')
    created_at = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback from {self.coach.__str__ if self.coach else 'Unknown'} to {self.student.__str__}"

class Badge(models.Model):
    label = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.label
    
class StudentBadge(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name='awarded_to')
    achieved_at = models.DateTimeField()

    class Meta:
        unique_together = ('student', 'badge')

    def __str__(self):
        return f"{self.student.__str__} - {self.badge.label}"    