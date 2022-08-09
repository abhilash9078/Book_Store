from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
import logging
from rest_framework.views import APIView
from user.serializers import (UserLoginSerializer,
                              UserProfileSerializer,
                              UserRegistrationSerializer,
                              UserProfileVerificationSerializer,
                              UserProfileVerificationEmailSerializer)
from django.contrib.auth import authenticate
from user.renderers import UserRenderer
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from user.token import JWT


logger = logging.getLogger('django')


# def get_tokens_for_user(user):
#     """
#     function for creating token for user
#     """
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


class UserRegistrationView(APIView):
    """
    API for performing user registration
    """
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        """
        post method for registering a user
        """
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info("User successfully Registered ")
            activate_serializer = UserProfileVerificationEmailSerializer(data=request.data)
            activate_serializer.is_valid(raise_exception=True)
            logger.info("Verification email send successfully ")
            return Response({'success': True, 'message': 'Registration Successful, Please verified your Email',
                             'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Registration Unsuccessful, Something went wrong',
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileVerificationView(APIView):
    """
    API for user account verification
    """
    renderer_classes = [UserRenderer]

    def post(self, request, uid, format=None):
        """
        post method for verifying user account
        """
        try:
            serializer = UserProfileVerificationSerializer(data=request.data, context={'uid': uid})
            serializer.is_valid(raise_exception=True)
            logger.info("User Profile is Successfully verified ")
            return Response({'success': True,
                             'msg': 'User Profile is Successfully verified '}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Something Went Wrong',
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    API for performing login operation
    """
    # renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        """
        post method for checking login operation
        """
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(**serializer.data)
            if user is not None:
                token = JWT.encode({"user_id": user.id})
                # logger.info("User is successfully logged in")
                return Response({'success': True, 'message': 'Login Successfully ',
                                 'data': {'token': token}}, status=status.HTTP_200_OK)
            else:
                logger.error("Something went wrong in password or email")
                return Response({'success': False, 'message': 'Login failed!',
                                 'data': {'username': serializer.data.get('username')}},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Login failed!, Something Went Wrong',
                             'data': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    """
    API for checking user details
    """
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        get function for checking user details
        """
        try:
            serializer = UserProfileSerializer(request.user)
            logger.info("User successfully access the profile")
            return Response({'success': True, 'message': 'User Profile',
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': 'Something Went Wrong',
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)



