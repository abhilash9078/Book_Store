from rest_framework import serializers
from order.models import Order


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'book_id', 'quantity']


class GetWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class EditWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['quantity']
