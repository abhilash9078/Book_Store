from django.test import TestCase
from django.urls import resolve
from user.models import User
from django.urls import reverse
from rest_framework import status
from book.models import Book


class TestBookAppURL(TestCase):
    """
    test class for testing book url
    """

    def test_add_book_url(self):
        """
        test function for testing add book url
        """
        path = reverse('add_book')
        assert resolve(path).view_name == 'add_book'

    def test_get_all_book_url(self):
        """
        test function for testing get all book url
        """
        path = reverse('all_book')
        assert resolve(path).view_name == 'all_book'


class TestBookView(TestCase):
    """
    Test class for Book CRUD operation view
    """

    def test_add_book_correct_data(self):
        """
        Test function for testing add book with correct data
        """
        User.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                 password='12345678', password2='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['tokens']
        # email = response.data['email']
        # user = User.objects.get(email=email)
        # user.is_verified = True
        # user.is_admin = True
        url2 = reverse('add_book')
        data2 = {'id': '8', 'book_name': 'test', 'author': 'me',
                 'price': '100', 'description': 'all about test', 'original_quantity': '5'}
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response2 = self.client.post(url2, data2, **header, format='json')
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

    # def test_all_book_correct_data(self):
    #     """
    #     Test function for testing all book with correct data
    #     """
    #     url = reverse('all_book')
    #     response = self.client.post(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
