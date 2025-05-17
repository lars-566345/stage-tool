def cookie_jwt_middleware(next, root, info, **kwargs):
    request = info.context
    jwt_cookie = request.COOKIES.get('jwt')
    if jwt_cookie and not request.META.get('HTTP_AUTHORIZATION'):
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {jwt_cookie}'
    return next(root, info, **kwargs)