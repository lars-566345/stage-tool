from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models.fix import StudentProfile, CoachProfile, Timeline, StudentPhaseProgress, StudentDeliverableProgress

@receiver(m2m_changed, sender=User.groups.through)
def handle_user_group_changes(sender, instance, action, pk_set, **kwargs):
    if action != "post_add":
        return
    
    if instance.is_superuser:
        return
    
    group_names = Group.objects.filter(pk__in=pk_set).values_list('name', flat=True)

    if 'Coach' in group_names:
        if not hasattr(instance, 'coach_profile'):
            CoachProfile.objects.create(user=instance)

    if 'Student' in group_names:
        if not hasattr(instance, 'student_profile'):
                    timeline = Timeline.objects.first()

        if not hasattr(instance, 'student_profile'):
            student = StudentProfile.objects.create(user=instance, timeline=timeline)
                
            if timeline:
                phases = timeline.phases.all().order_by('order')
                StudentPhaseProgress.objects.bulk_create([
                    StudentPhaseProgress(student=student, phase=phase)
                    for phase in phases
                ])

                deliverables = []
                for phase in phases:
                    deliverables.extend([
                        StudentDeliverableProgress(student=student, deliverable=deliverable, phase=phase)
                        for deliverable in phase.deliverables.all()
                    ])

                StudentDeliverableProgress.objects.bulk_create(deliverables)