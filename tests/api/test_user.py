import pytest
from rest_framework.test import APIClient
from django import urls
from django.contrib.auth import get_user_model


# client = APIClient()


# @pytest.mark.parametrize('param', ["register", "login"])
# def test_render_view(client, param):
#     temp_url = urls.reverse(param)
#     resp = client.get(temp_url)
#     assert resp.status_code == 405


@pytest.mark.django_db
def test_user_register(client, user_data):
    user_model = get_user_model()
    assert user_model.count() == 0



