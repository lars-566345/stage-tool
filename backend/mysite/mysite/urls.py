from django.urls import path
from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from core.graphql.views import CustomGraphQLView, get_csrf_token
from core.graphql.schema import schema
from core.graphql.middleware import LoginRequiredMiddleware, JWTAuthenticationMiddleware

urlpatterns = [
    path(
        "graphql/",
        csrf_protect(
            CustomGraphQLView.as_view(
                graphiql=True,
                schema=schema,
                middleware=[
                    JWTAuthenticationMiddleware(),
                    LoginRequiredMiddleware(),
                ]
            )
        ),
    ),
    path("csrf/", get_csrf_token),
    path('admin/', admin.site.urls),
]
