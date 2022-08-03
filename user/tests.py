from django.test import TestCase
from django.urls import resolve
from user.models import User
from django.urls import reverse
from rest_framework import status


class TestLoginRegistrationURL(TestCase):
    """
    test class for testing user url
    """
    def test_login_user_url(self):
        """
        test function for testing user login url
        """
        path = reverse('login')
        assert resolve(path).view_name == 'login'

    def test_registration_user_url(self):
        """
        test function for testing user registration url
        """
        path = reverse('register')
        assert resolve(path).view_name == 'register'

    def test_profile_user_url(self):
        """
        test function for testing user profile url
        """
        path = reverse('profile')
        assert resolve(path).view_name == 'profile'


class TestLoginRegistrationModel(TestCase):
    """
    test class for testing User model
    """
    def test_should_create_user(self):
        user = User.objects.create_user(username='abhilash', email='abhilash@gmail.com', mobile_no=123456678)
        user.set_password("12345678")
        user.save()
        self.assertEqual(str(user), 'abhilash@gmail.com')


class TestLoginRegistrationView(TestCase):
    """
    Test class for User Login and Registration view
    """
    def test_create_user_with_correct_data(self):
        """
        Test function for testing user registration with correct data
        """
        url = reverse('register')
        data = {'username': 'abhi', 'email': 'abhi@gmail.com', 'mobile_no': '45612378',
                'password': '12345678', 'password2': '12345678'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_with_incorrect_data(self):
        """
        Test function for testing user registration View with incorrect data
        """
        url = reverse('register')
        data = {'username': 'admin', 'email': 'admin@gmail.com', 'mobile_no': '907815429',
                'password': '12345678'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_correct_input_success(self):
        """
        Test function for testing User Login view with correct data
        """
        credentials = {
            'username': 'admin',
            'mobile_no': 456123785,
            'email': 'admin@gmail.com',
            'password': '12345678'}
        User.objects.create_user(**credentials)
        url = reverse('login')
        response = self.client.post(url, credentials, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_with_incorrect_input_success(self):
        """
        Test function for testing user login View with incorrect data
        """
        credentials = {
            'username': 'admin',
            'mobile_no': 456123785,
            'email': 'admin@gmail.com',
            'password': '12345678'}
        User.objects.create_user(**credentials)
        url = reverse('login')
        login_data = {
            'email': 'admin@gmail.com',
            'password': '1234567'}
        response = self.client.post(url, login_data, follow=True)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
