import jwt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from graphql import GraphQLError

import logging
logger = logging.getLogger(__name__)

User = get_user_model()

class JWTAndLoginRequiredMiddleware:
    EXEMPT_OPERATIONS = ["login", "success", "errors", "token", "admin", "me"]

    def resolve(self, next, root, info, **kwargs): 
        request = info.context
        token = request.COOKIES.get("jwt")

        # Standaard user = anonymous
        request.user = AnonymousUser()
        info.context.user = AnonymousUser()

        # JWT authenticatie
        if token:
            logger.warning(f"JWT token found: {token}")
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                logger.warning(f"Decoded JWT payload: {payload}")
                username = payload.get("username")
                if username:
                    user = User.objects.filter(username=username).first()
                    if user:
                        logger.warning(f"Authenticated user: {user}")
                        request.user = user
                        info.context.user = user
                    else:
                        logger.warning(f"No user found with username: {username}")
                else:
                    logger.warning("Username not in JWT payload")
            except Exception as e:
                logger.error(f"JWT decode error: {e}")

        # LoginRequired check
        operation_name = info.field_name.strip().lower()
        exempt_ops = {op.strip().lower() for op in self.EXEMPT_OPERATIONS}
        logger.warning(f"LoginRequiredMiddleware: Operation - {operation_name}, User Authenticated - {info.context.user.is_authenticated}")
        logger.warning(f"LoginRequiredMiddleware: Operation - '{operation_name}', Exempt Operations - {self.EXEMPT_OPERATIONS}")


        if operation_name not in exempt_ops:
            user = info.context.user
            if not user or not user.is_authenticated:
                logger.warning("LoginRequiredMiddleware: Authentication required error raised.")
                raise GraphQLError("Authentication required.")

        # Ga door naar de volgende resolver
        return next(root, info, **kwargs)
