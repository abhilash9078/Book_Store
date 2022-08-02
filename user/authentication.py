from rest_framework import status
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
            return Response({"message": "Authorization error"}, status=status.HTTP_400_BAD_REQUEST)
        token_type, token_string = request.headers.get("Authorization").split()
        payload = JWT.decode(token_string)
        user = User.objects.get(id=payload.get("user_id"))
        if not user.is_verified:
            return Response({'success': False,
                             'message': "Only verified user can perform this action"},
                            status=status.HTTP_404_NOT_FOUND)
        request.user = user
        return func(*args, **kwargs)
    return wrapper
