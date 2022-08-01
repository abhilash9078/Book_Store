from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.CartAPIView.as_view(), name="adding_to_cart"),
    path('view_cart/', views.CartAPIView.as_view(), name="view_cart"),
    path('delete/<id>', views.CartAPIView.as_view(), name="delete_cart_item"),
    path('update/<id>', views.CartAPIView.as_view(), name="update_cart_item"),
]
