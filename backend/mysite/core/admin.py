from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.html import format_html, format_html_join

from django import forms

from .models import *

class CoachStudentInline(admin.TabularInline):
    model = CoachStudent
    extra = 1

# Custom user creation
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            self.save_m2m()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'groups'),
        }),
    )

# Unregister default User Admin
admin.site.unregister(User)

# Register Custom User Admin
admin.site.register(User, CustomUserAdmin)



# Register your models here.
@admin.register(KnowledgeBaseArticle)
class KnowledgeBaseArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Deliverable)
class DeliverableAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Phase)
class PhaseAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'identity')
    search_fields = ('title', 'identity')
    filter_horizontal = ('deliverables',)

@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('id',)
    filter_horizontal = ('phases',)

@admin.register(CoachProfile)
class CoachProfileAdmin(admin.ModelAdmin):
    inlines = [CoachStudentInline]
    list_display = ('user',)
    search_fields = ('user__first_name', 'user__last_name')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    inlines = [CoachStudentInline]
    list_display = ('user', 'timeline')
    search_fields = ('user__first_name', 'user__last_name')
    filter_horizontal = ('favorite_articles',)

    def get_coaches(self, obj):
        return ", ".join([
            f"{cs.coach.user.first_name} {cs.coach.user.last_name}"
            for cs in obj.student_coach.all()
        ])
    get_coaches.short_description = 'Coaches'

@admin.register(StudentPhaseProgress)
class StudentPhaseProgressAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'phase', 'status', 'updated_at')
    list_fitler = ('status', 'updated_at')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'phase__title')

    @admin.display(ordering='student__user__last_name', description='Student')
    def get_student_name(self, obj):
        user = obj.student.user
        if user:
            return f"{user.first_name} {user.last_name}"
        return "-"


@admin.register(StudentDeliverableProgress)
class StudentDeliverableProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'deliverable', 'phase', 'submitted', 'submitted_at')
    list_fitler = ('submitted', 'submitted_at')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'deliverable__title', 'phase__title')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('student', 'coach', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('student__user__first_name', 'student__user__last_name', 'coach__user__first_name', 'coach__user__last_name')

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('label',)
    search_fields = ('label',)

@admin.register(StudentBadge)
class StudentBadgeAdmin(admin.ModelAdmin):
    list_display = ('student', 'badge', 'achieved_at')
    list_filter = ('achieved_at', 'badge')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'badge__label')