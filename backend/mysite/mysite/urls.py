from django.urls import path
from django.views.decorators.csrf import csrf_protect
from core.graphql.views import CustomGraphQLView
from core.graphql.schema import schema

urlpatterns = [
    path(
        "graphql/",
        csrf_protect(
            CustomGraphQLView.as_view(
                graphiql=True,
                schema=schema,
            )
        ),
    ),
]
