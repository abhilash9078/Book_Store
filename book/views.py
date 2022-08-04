from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from user.authentication import verify_token
from .models import Book
from book.serializers import BookSerializer, AllBookListSerializer


def book_validator(data):
    """
    function for validating books
    """
    bid = data.get('id')
    book = Book.objects.filter(id=bid).first()
    if book:
        return Response({'success': False,
                         'message': "Books is already exists"}, status=status.HTTP_404_NOT_FOUND)


class GetAllBookListView(GenericAPIView):
    def get(self, request):
        try:
            book_list = Book.objects.order_by('id')
            serializer = AllBookListSerializer(book_list, many=True)
            return Response({'success': True,
                             'message': "All Book",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went Wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BookAPIView(GenericAPIView):
    serializer_class = BookSerializer

    @verify_token
    def post(self, request):
        try:
            if not request.user.is_admin:
                return Response({'success': False,
                                 'message': "Only admin can perform this action"}, status=status.HTTP_404_NOT_FOUND)
            data = request.data
            validated_data = book_validator(data)
            if validated_data:
                book = Book.objects.get(id=data.get('id'))
                book.quantity_now = book.quantity_now + int(data.get('original_quantity'))
                book.save()
                return Response({'success': True,
                                 'message': "Book is already exists, only quantity is updated"},
                                status=status.HTTP_200_OK)
            book = Book.objects.create(**data, quantity_now=data.get('original_quantity'))
            book.save()
            return Response({'success': True,
                             'message': "New Book Added Successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def put(self, request, pk):
        try:
            if not request.user.is_admin:
                return Response({'success': False,
                                 'message': "Only admin can perform this action"}, status=status.HTTP_404_NOT_FOUND)
            book = Book.objects.get(id=pk)
            if not book:
                return Response({'success': False,
                                 'message': "Book Not Found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = BookSerializer(instance=book, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response({'success': True,
                             'message': "Book is successfully updated",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self, request, pk):
        try:
            if not request.user.is_admin:
                return Response({'success': False,
                                 'message': "Only admin can perform this action"}, status=status.HTTP_404_NOT_FOUND)
            book = Book.objects.get(id=pk)
            if not book:
                return Response({'success': False,
                                 'message': "Book Not Found"}, status=status.HTTP_404_NOT_FOUND)
            book.delete()
            return Response({'success': True,
                             'message': "Book is successfully deleted",
                             'data': book.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


