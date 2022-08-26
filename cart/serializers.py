from rest_framework import serializers
from order.models import Order


class CartSerializer(serializers.ModelSerializer):
    """
    serializer class for adding cart item
    """
    class Meta:
        model = Order
        fields = ['id', 'book_id', 'quantity', 'user_id']


class GetCartSerializer(serializers.ModelSerializer):
    """
    serializer class for getting all the cart item
    """
    class Meta:
        model = Order
        fields = ['id', 'book_id', 'quantity', 'total_price']


class EditCartSerializer(serializers.ModelSerializer):
    """
    serializer class for edit cart item
    """
    class Meta:
        model = Order
        fields = ['quantity']
