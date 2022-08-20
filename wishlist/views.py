from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from book.models import Book
from order.models import Order, OrderStatus
from wishlist.serializers import WishlistSerializer, GetWishlistSerializer
from user.authentication import verify_token


class WishlistAPIView(GenericAPIView):
    serializer_class = WishlistSerializer

    @verify_token
    def post(self, request):
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
            return Response({'success': True,
                             'message': "Successfully added to wishlist"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def get(self, request):
        try:
            wish = Order.objects.filter(user_id=request.user)
            wish.status = OrderStatus.w.value
            serializer = GetWishlistSerializer(instance=wish, many=True)
            return Response({'success': True,
                             'message': "Wishlist Items",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self, request, id):
        try:
            wish = Order.objects.get(id=id)
            wish.status = OrderStatus.w.value
            wish.delete()
            return Response({'success': True,
                             'message': "Successfully deleted "}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

