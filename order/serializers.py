from rest_framework import serializers
from order.models import Order
from book.models import Book


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['shipping_address']


class AddRatingsToBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ratings']
