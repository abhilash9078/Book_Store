from rest_framework.request import Request
from rest_framework.response import Response

from user.models import User
from user.token import JWT


def verify_token(func):
    """
    function for checking and verifying token for valid user
    """
    def wrapper(*args, **kwargs):
        request = list(filter(lambda x: isinstance(x, Request), args))[0] or kwargs.get("request")

        if "Authorization" not in request.headers:
            return Response({"message": "Autho"})
        token_type, token_string = request.headers.get("Authorization").split()
        payload = JWT.decode(token_string)
        request.user = User.objects.get(id=payload.get("user_id"))
        return func(*args, **kwargs)
    return wrapper
