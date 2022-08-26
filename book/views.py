from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
import logging
from user.authentication import verify_token
from .models import Book
from book.serializers import BookSerializer, AllBookListSerializer


logger = logging.getLogger('django')


class GetAllBookListView(GenericAPIView):
    """
    Class view for getting all the book
    """
    def get(self, request):
        """
        get function for requesting get method to get all the book
        """
        try:
            book_list = Book.objects.order_by('id')
            serializer = AllBookListSerializer(book_list, many=True)
            paginator = Paginator(book_list, 5)
            page_number = request.data.get('page')
            page_obj = paginator.get_page(page_number)
            logger.info("Getting all the book successfully")
            return Response({'success': True,
                             'message': "All Book",
                             'data': serializer.data,
                             'page': str(page_obj)}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went Wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BookAPIView(GenericAPIView):
    """
    class view for Book api crud operation
    """
    serializer_class = BookSerializer

    @verify_token
    def post(self, request):
        """
        post function for post request to add book
        """
        try:
            if not request.user.is_admin:
                logger.error("not admin task")
                return Response({'success': False,
                                 'message': "Only admin can perform this action"}, status=status.HTTP_404_NOT_FOUND)

            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info("Successfully added the book")
            return Response({'success': True,
                             'message': "New Book Added Successfully",
                             'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def put(self, request, pk):
        """
        put function for put request to update book
        """
        try:
            if not request.user.is_admin:
                logger.error("not admin task")
                return Response({'success': False,
                                 'message': "Only admin can perform this action"}, status=status.HTTP_404_NOT_FOUND)
            book = Book.objects.get(id=pk)
            if not book:
                logger.error("book not found")
                return Response({'success': False,
                                 'message': "Book Not Found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = BookSerializer(instance=book, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            logger.info("Book updated successfully ")
            return Response({'success': True,
                             'message': "Book is successfully updated",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self, request, pk):
        """
        delete function for delete request to delete a book
        """
        try:
            if not request.user.is_admin:
                logger.error("not admin task")
                return Response({'success': False,
                                 'message': "Only admin can perform this action"}, status=status.HTTP_404_NOT_FOUND)
            book = Book.objects.get(id=pk)
            if not book:
                logger.error("book not found ")
                return Response({'success': False,
                                 'message': "Book Not Found"}, status=status.HTTP_404_NOT_FOUND)
            book.delete()
            logger.info("successfully deleted the book")
            return Response({'success': True,
                             'message': "Book is successfully deleted",
                             'data': book.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


