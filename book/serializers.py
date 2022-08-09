from rest_framework import serializers
from .models import Book


class AllBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author', 'price', 'description', 'quantity_now', 'ratings']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author', 'price', 'original_quantity', 'description']
        required_field = ['book_name', 'author', 'price', 'original_quantity']

    def create(self, validated_data):
        validated_data.update({'quantity_now': validated_data.get('original_quantity')})
        return self.Meta.model.objects.create(**validated_data)

