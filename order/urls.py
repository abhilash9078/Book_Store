from django.urls import path
from .views import CheckoutAPIView

urlpatterns = [
    path('checkout/<int:cid>', CheckoutAPIView.as_view())
]
