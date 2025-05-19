import jwt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.COOKIES.get("jwt")
        request.user = AnonymousUser()

        if not token:
            return

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            username = payload.get("username")
            if username:
                user = User.objects.filter(username=username).first()
                if user:
                    request.user = user
        except Exception:
            pass

class LoginRequiredMiddleware(MiddlewareMixin):
    EXEMPT_OPERATIONS = ["login"]

    def resolve(self, next, root, info, **kwargs):
        # Only check at the root field level
        if root is None:
            if info.field_name.lower() in (op.lower() for op in self.EXEMPT_OPERATIONS):
                return next(root, info, **kwargs)

            print(info.context.user)
            user = info.context.user
            if not user or not user.is_authenticated:
                from graphql import GraphQLError
                raise GraphQLError("Authentication required.")

        # For subfields, just continue without checking again
        return next(root, info, **kwargs)
