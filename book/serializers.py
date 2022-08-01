from rest_framework import serializers
from .models import Book


class AllBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author', 'price', 'description', 'quantity_now']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author', 'price', 'original_quantity', 'description']
        required_field = ['id', 'book_name', 'author', 'price', 'original_quantity']

