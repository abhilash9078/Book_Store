from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from book.models import Book
from order.models import Order, OrderStatus
from wishlist.serializers import WishlistSerializer, GetWishlistSerializer
from user.authentication import verify_token
import logging

logger = logging.getLogger('django')


class WishlistAPIView(GenericAPIView):
    """
    class view for CRUD operation for wishlist app
    """
    serializer_class = WishlistSerializer

    @verify_token
    def post(self, request):
        """
        post function for post request to add item in wishlist
        """
        try:
            new_book = request.data
            book = Book.objects.get(id=new_book.get('book_id'))
            if not book:
                return Response({'success': False,
                                 'message': "Book is not found with this id",
                                 'data': book.id}, status=status.HTTP_404_NOT_FOUND)
            total_amt = book.price
            wishlist = Order.objects.create(
                user_id=request.user,
                book_id=book,
                quantity=1,
                total_price=total_amt
            )
            wishlist.status = OrderStatus.w.value
            wishlist.save()
            book.save()
            logger.info("Successfully added the item in wishlist")
            return Response({'success': True,
                             'message': "Successfully added to wishlist"}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def get(self, request):
        """
        function for get request to view all wishlist item
        """
        try:
            wish = Order.objects.filter(user_id=request.user)
            wish.status = OrderStatus.w.value
            serializer = GetWishlistSerializer(instance=wish, many=True)
            logger.info("all wishlist item")
            return Response({'success': True,
                             'message': "Wishlist Items",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self, request, id):
        """
        function for delete request to delete an item from wishlist
        """
        try:
            wish = Order.objects.get(id=id)
            wish.status = OrderStatus.w.value
            wish.delete()
            logger.info("successfully deleted ")
            return Response({'success': True,
                             'message': "Successfully deleted "}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

