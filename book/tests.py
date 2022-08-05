from django.test import TestCase
from django.urls import resolve
from user.models import User
from django.urls import reverse
from rest_framework import status
from book.models import Book
import json


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
        user = User.objects.create_superuser(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                             password='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('add_book')
        data2 = {'book_name': 'test', 'author': 'me',
                 'price': 100.99, 'description': 'all about test', 'original_quantity': 5}
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response2 = self.client.post(url2, data2, **header)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

    def test_add_book_incorrect_data(self):
        """
        Test function for testing add book with incorrect data
        """
        user = User.objects.create_superuser(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                             password='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('add_book')
        data2 = {'author': 'me',
                 'price': 100.99, 'description': 'all about test', 'original_quantity': 5}
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response2 = self.client.post(url2, data2, **header)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_update_book_incorrect_data(self):
    #     """
    #     Test function for testing add book with incorrect data
    #     """
    #     user = User.objects.create_superuser(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
    #                                          password='12345678')
    #     url = reverse('login')
    #     data = {'email': 'abhi@gmail.com', 'password': '12345678'}
    #     response = self.client.post(url, data, format='json')
    #     token = response.data['data']['token'].decode('utf-8')
    #     url2 = reverse('add_book')
    #     data2 = {'book_name': 'test', 'author': 'me',
    #              'price': 100.99, 'description': 'all about test', 'original_quantity': 5}
    #     header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
    #     response2 = self.client.post(url2, data2, **header)
    #     book_id = response2.data['data']['id']
    #     url3 = reverse('update_book')
    #     data3 = {'book_name': 'test', 'author': 'me',
    #              'price': 100.99, 'description': 'all about test', 'original_quantity': 5}
    #     header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
    #     response3 = self.client.put(url3/book_id, data3, **header)
    #
    #     self.assertEqual(response3.status_code, status.HTTP_200_OK)
