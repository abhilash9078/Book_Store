from django.urls import path
from .views import CheckoutAPIView, AddRatingsAPIView

urlpatterns = [
    path('checkout/<int:cid>', CheckoutAPIView.as_view()),
    path('add_rating/<int:bid>', AddRatingsAPIView.as_view())
]
