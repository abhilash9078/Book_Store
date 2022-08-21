from rest_framework import serializers
from order.models import Order


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'book_id']


class GetWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'book_id', 'total_price']



