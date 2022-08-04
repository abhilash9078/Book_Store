import pytest
from django.urls import reverse


pytest_mark = pytest.mark.django_db


class TestRegistrationAndLoginApiView:

    @pytest.mark.django_db
    def test_as_login_successfully(self, client, django_user_model):
        user = django_user_model.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no=123456789,
                                                     password='12345678', password2='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = client.post(url, data, content_type="application/json")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_as_login_unsuccessful(self, client, django_user_model):
        user = django_user_model.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no=123456789,
                                                     password='12345678', password2='12345678')
        url = reverse('login')
        data = {'username': 'abhi@gmail.com', 'password': '12345678'}
        response = client.post(url, data, content_type="application/json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_as_registration_successfully(self, client, django_user_model):
        url = reverse('register')
        data = {'username': 'abhi', 'email': 'abhi@gmail.com', 'mobile_no': '45612378',
                'password': '12345678', 'password2': '12345678'}
        response = client.post(url, data, format='json', content_type="application/json")
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_as_registration_unsuccessful(self, client, django_user_model):
        url = reverse('register')
        data = {'username': 'abhi', 'email': 'abhi@gmail.com', 'mobile_no': '45612378',
                'password': '12345678'}
        response = client.post(url, data, format='json', content_type="application/json")
        assert response.status_code == 400





