import pytest
from django.urls import reverse
from user.models import User

pytest_mark = pytest.mark.django_db


class TestBookApiView:

    @pytest.mark.get_book
    def test_get_all_book_successfully(self, client, django_user_model, db):
        url = reverse('all_book')
        response = client.get(url, content_type="application/json")
        assert response.status_code == 200

    @pytest.mark.add_book
    def test_add_book_correct_data(self, client, django_user_model, db):
        """
        Test function for testing add book with correct data
        """
        user = User.objects.create_superuser(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                             password='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('add_book')
        data2 = {'book_name': 'test', 'author': 'me',
                 'price': 100.99, 'description': 'all about test', 'original_quantity': 5}
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response2 = client.post(url2, data2, **header)
        assert response2.status_code == 201

    @pytest.mark.django_db
    def test_add_book_with_incorrect_data(self, client, django_user_model):
        """
        Test function for testing add book with incorrect data
        """
        user = User.objects.create_superuser(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                             password='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('add_book')
        data2 = {'author': 'me',
                 'price': 100.99, 'description': 'all about test', 'original_quantity': 5}
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response2 = client.post(url2, data2, **header)
        assert response2.status_code == 400

    # @pytest.mark.update_book
    # def test_update_book_with_correct_data(self, client, django_user_model, db):
    #     """
    #     Test function for testing update book with correct data
    #     """
    #     user = User.objects.create_superuser(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
    #                                          password='12345678')
    #     url = reverse('login')
    #     data = {'email': 'abhi@gmail.com', 'password': '12345678'}
    #     response = client.post(url, data, format='json')
    #     token = response.data['data']['token'].decode('utf-8')
    #     header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
    #     print(response.data)
    #     url2 = reverse('update_book')
    #     data2 = {'book_name': 'test', 'author': 'me',
    #              'price': 100.99, 'description': 'all about test', 'original_quantity': 6}
    #
    #     response2 = client.post(url2, data2, **header)
    #     assert response2.status_code == 200
