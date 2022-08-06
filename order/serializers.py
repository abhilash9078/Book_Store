from rest_framework import serializers
from .models import Order


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['shipping_address']
