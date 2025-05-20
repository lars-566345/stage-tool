import jwt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from graphql import GraphQLError

User = get_user_model()

class JWTAuthenticationMiddleware:
    def resolve(self, next, root, info, **kwargs):
        request = info.context
        token = request.COOKIES.get("jwt")
        request.user = AnonymousUser()

        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                username = payload.get("username")
                if username:
                    user = User.objects.filter(username=username).first()
                    if user:
                        request.user = user
            except Exception:
                pass

        return next(root, info, **kwargs)


class LoginRequiredMiddleware:
    EXEMPT_OPERATIONS = ["login", "admin"]

    def resolve(self, next, root, info, **kwargs):
        if root is None:
            operation_name = info.field_name.lower()
            if operation_name in (op.lower() for op in self.EXEMPT_OPERATIONS):
                return next(root, info, **kwargs)

            user = info.context.user
            if not user or not user.is_authenticated:
                raise GraphQLError("Authentication required.")

        return next(root, info, **kwargs)