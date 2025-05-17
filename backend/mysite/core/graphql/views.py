import json
from django.middleware.csrf import get_token
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

class CustomGraphQLView(GraphQLView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def _is_csrf_exempt_mutation(self, request):
        if request.method.lower() != 'post':
            return False
        try:
            body = json.loads(request.body)
            query = body.get("query", "")
            return any(name in query for name in ["login", "refreshToken"])
        except Exception:
            return False

    def _is_csrf_exempt_mutation(self, request):
        if request.method.lower() != 'post':
            return False

        try:
            body = json.loads(request.body)
            query = body.get("query", "")
            return any(name in query for name in ["login", "refreshToken"])
        except Exception:
            return False
