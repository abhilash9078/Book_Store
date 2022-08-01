from rest_framework import serializers
from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'book_id', 'quantity']


class GetCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class EditCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity']
