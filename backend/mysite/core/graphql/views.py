# myapp/views.py

from graphene_django.views import GraphQLView
from django.middleware.csrf import get_token

class CustomGraphQLView(GraphQLView):
    def dispatch(self, request, *args, **kwargs):

        # Set CSRF cookie
        get_token(request)

        response = super().dispatch(request, *args, **kwargs)

        token = getattr(request, 'jwt_cookie', None)
        if token:
            response.set_cookie(
                key='jwt',
                value=token,
                httponly=True,
                secure=False,
                samesite='Lax',
                path='/',
                max_age=60 * 60 * 24,
            )
        return response
