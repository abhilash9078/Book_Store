from rest_framework import serializers
from user.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from user.utils import Util


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    serializer class for user registration
    """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'mobile_no', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")

        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserProfileVerificationEmailSerializer(serializers.Serializer):
    """
    serializer class for profile verification of user
    """
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            link = ' http://127.0.0.1:8000/user/verify_account/' + uid + '/'
            body = 'Click Following Link to Activate Your Account ' + link
            data = {
                'subject': 'Activate Your Account',
                'body': body,
                'to_email': user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError('You are not a Registered User')


class UserProfileVerificationSerializer(serializers.Serializer):
    """
    serializer class for profile verification
    """

    def validate(self, attrs):
        try:
            uid = self.context.get('uid')
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            user.is_verified = True
            user.save()
            return attrs
        except Exception as e:
            raise serializers.ValidationError(f"Something went wrong {e}")


class UserLoginSerializer(serializers.ModelSerializer):
    """
    serializer class for login of user
    """
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    """
    serializer class for profile view of user
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'mobile_no', 'is_verified', 'is_admin']

