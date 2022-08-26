from django.test import TestCase
from django.urls import resolve
from user.models import User
from django.urls import reverse
from rest_framework import status


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



