from graphql import GraphQLError

EXEMPT_OPERATIONS = ["login", "tokenAuth", "refreshToken", "verifyToken", "revokeToken"]

def login_required_middleware(next, root, info, **kwargs):
    field_name = info.field_name
    if field_name in EXEMPT_OPERATIONS:
        return next(root, info, **kwargs)
    user = info.context.user
    if not user or not user.is_authenticated:
        raise GraphQLError("Authentication required.")
    return next(root, info, **kwargs)