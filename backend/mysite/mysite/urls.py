from django.contrib import admin
from django.urls import path
from graphene.validation import depth_limit_validator, DisableIntrospection
from django.views.decorators.csrf import csrf_protect

from core.graphql.schema import schema
from core.graphql.views import CustomGraphQLView
from core.graphql.middleware.cookie import cookie_jwt_middleware
from core.graphql.middleware.login import login_required_middleware

#Add specific schema's/rework apolloclient in react to not require Introspection
validation_rules = [
    depth_limit_validator(max_depth=3),
    #DisableIntrospection
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", csrf_protect(CustomGraphQLView.as_view(
        graphiql=True,
        schema=schema,
        validation_rules=validation_rules,
        middleware=[cookie_jwt_middleware, login_required_middleware ]
    ))),
]
