from rest_framework import serializers
from order.models import Order


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'book_id', 'quantity', 'user_id']


class GetCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'book_id', 'quantity', 'total_price']


class EditCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['quantity']
