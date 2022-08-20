from django.urls import path
from wishlist import views


urlpatterns = [
    path('add/', views.WishlistAPIView.as_view(), name="adding_to_wishlist"),
    path('view/', views.WishlistAPIView.as_view(), name="view_wishlist"),
    path('delete/<int:id>', views.WishlistAPIView.as_view(), name="delete_wishlist_item"),
]
