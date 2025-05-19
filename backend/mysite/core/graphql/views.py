from graphene_django.views import GraphQLView
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

class CustomGraphQLView(GraphQLView):
    def dispatch(self, request, *args, **kwargs):
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

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"detail": "CSRF cookie set"})