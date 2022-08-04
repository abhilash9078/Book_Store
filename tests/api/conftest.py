import pytest
from django.urls import reverse


@pytest.fixture
def user_data():
    return {'email': 'book@gmail.com',
            'username': 'book',
            'mobile_no': 45612378,
            'password': 'book123',
            'password2': 'book123'}


@pytest.fixture
def authentication_user(client, django_user_model):
    user = django_user_model.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no=123456789,
                                                 password='12345678', password2='12345678')
    url = reverse('login')
    data = {'email': 'abhi@gmail.com', 'password': '12345678'}
    client.post(url, data)
    return user.id

