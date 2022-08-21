from django.test import TestCase
from django.urls import resolve
from user.models import User
from django.urls import reverse
from rest_framework import status
from book.models import Book


class TestCartAppURL(TestCase):
    """
    test class for testing Cart url
    """

    def test_add_to_cart_url(self):
        """
        test function for testing add to cart url
        """
        path = reverse('adding_to_cart')
        assert resolve(path).view_name == 'adding_to_cart'

    def test_get_all_cart_url(self):
        """
        test function for testing get all cart url
        """
        path = reverse('view_cart')
        assert resolve(path).view_name == 'view_cart'

    def test_update_cart_url(self):
        """
        test function for testing get all cart url
        """
        path = reverse('update_cart_item', kwargs={'id': 1})
        print(resolve(path).view_name, "updated value")
        assert resolve(path).view_name == 'update_cart_item'


class TestCartView(TestCase):
    """
    Test class for cart CRUD operation view
    """

    def test_view_cart_correct_data(self):
        """
        Test function for testing view cart with correct data
        """
        user = User.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                        password='12345678', password2='12345678', is_verified=True)
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('view_cart')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response2 = self.client.get(url2, **header)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_view_cart_incorrect_data(self):
        """
        Test function for testing view cart with incorrect data
        """
        user = User.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                        password='12345678', password2='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('view_cart')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response2 = self.client.get(url2, **header)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_to_cart_correct_data(self):
        """
        Test function for testing add to cart with correct data
        """
        user = User.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                        password='12345678', password2='12345678', is_verified=True)
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('adding_to_cart')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        data2 = {'id': '2', 'book_id': '2', 'quantity': '5'}
        response2 = self.client.get(url2, data2, **header)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_add_to_cart_incorrect_data(self):
        """
        Test function for testing add to cart with incorrect data
        """
        user = User.objects.create_user(username='abhi', email='abhi@gmail.com', mobile_no='456123784',
                                        password='12345678', password2='12345678')
        url = reverse('login')
        data = {'email': 'abhi@gmail.com', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        token = response.data['data']['token'].decode('utf-8')

        url2 = reverse('adding_to_cart')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        data2 = {'id': '2', 'book_id': '2', 'quantity': '5'}
        response2 = self.client.get(url2, data2, **header)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
