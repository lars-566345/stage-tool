from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(Badge)
admin.site.register(Evaluation)
admin.site.register(Phase)
admin.site.register(Profile)
admin.site.register(TeacherStudent)

admin.site.register(ArticlePhase)
admin.site.register(UserBadge)