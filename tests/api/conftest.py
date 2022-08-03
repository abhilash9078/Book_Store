import pytest


@pytest.fixture
def user_data():
    return {'email': 'book@gmail.com',
            'username': 'book',
            'mobile_no': 45612378,
            'password': 'book123',
            'password2': 'book123'}
