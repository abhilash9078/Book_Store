import pytest
from django.urls import reverse


pytest_mark = pytest.mark.django_db


# class TestBookApiView:
#
#     @pytest.mark.django_db
#     def test_get_all_book_successfully(self, client, django_user_model):
#         url = reverse('all_book')
#         data = {'username': 'abhi', 'email': 'abhi@gmail.com', 'mobile_no': '45612378',
#                 'password': '12345678', 'password2': '12345678'}
#         response = client.post(url, data, format='json', content_type="application/json")
#         assert response.status_code == 200
        