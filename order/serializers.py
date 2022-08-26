from rest_framework import serializers
from order.models import Order
from book.models import Book


class CheckoutSerializer(serializers.ModelSerializer):
    """
    serializer class for order app
    """
    class Meta:
        model = Order
        fields = ['shipping_address']


