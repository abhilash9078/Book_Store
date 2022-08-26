from rest_framework import serializers
from order.models import Order


class WishlistSerializer(serializers.ModelSerializer):
    """
    serializer class for adding item to wishlist
    """
    class Meta:
        model = Order
        fields = ['id', 'book_id']


class GetWishlistSerializer(serializers.ModelSerializer):
    """
    serializer class for view all wishlist item
    """
    class Meta:
        model = Order
        fields = ['id', 'book_id', 'total_price']



