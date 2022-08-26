import jwt
from datetime import timedelta, datetime
from django.conf import settings


class JWT:
    """
    class for generating token
    """
    @staticmethod
    def encode(payload):
        payload.update({"exp": datetime.now()+timedelta(minutes=settings.JWT_EXP_TIME)})
        return jwt.encode(payload, settings.JWT_SECRET_KEY, "HS256")

    @staticmethod
    def decode(token):
        return jwt.decode(token, settings.JWT_SECRET_KEY, ["HS256"])

