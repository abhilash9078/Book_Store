from django.urls import path
from user.views import UserLoginView, UserRegistrationView, UserProfileView, UserProfileVerificationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('verify_account/<uid>/', UserProfileVerificationView.as_view(), name='verification'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),

]
