from django.test import TestCase
from django.urls import resolve
from user.models import User
from django.urls import reverse
from rest_framework import status
from book.models import Book


class TestWishlistAppURL(TestCase):
    """
    test class for testing Wishlist url
    """

    def test_add_to_wishlist_url(self):
        """
        test function for testing add to wishlist url
        """
        path = reverse('adding_to_wishlist')
        assert resolve(path).view_name == 'adding_to_wishlist'

    def test_get_all_wishlist_url(self):
        """
        test function for testing get all wishlist url
        """
        path = reverse('view_wishlist')
        assert resolve(path).view_name == 'view_wishlist'


class TestWishlistView(TestCase):
    """
    Test class for wishlist CRUD operation view
    """

    def test_view_wishlist_correct_data(self):
        """
        Test function for testing view wishlist with correct data
        """
        user = User.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                        password='12345678', password2='12345678', is_verified=True)
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('view_wishlist')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response2 = self.client.get(url2, **header)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_view_wishlist_incorrect_data(self):
        """
        Test function for testing view wishlist with incorrect data
        """
        user = User.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                        password='12345678', password2='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('view_wishlist')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response2 = self.client.get(url2, **header)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_to_wishlist_correct_data(self):
        """
        Test function for testing add to wishlist with correct data
        """
        user = User.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                        password='12345678', password2='12345678', is_verified=True)
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('adding_to_wishlist')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        data2 = {'id': '2', 'book_id': '2', 'quantity': '5'}
        response2 = self.client.get(url2, data2, **header)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_add_to_wishlist_incorrect_data(self):
        """
        Test function for testing add to wishlist with incorrect data
        """
        user = User.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                        password='12345678', password2='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('adding_to_wishlist')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        data2 = {'id': '2', 'book_id': '2', 'quantity': '5'}
        response2 = self.client.get(url2, data2, **header)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)


