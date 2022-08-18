from rest_framework import status
from rest_framework.views import APIView, Response
from user.models import User
from book.models import Book
from .models import Order, OrderStatus
from .serializers import CheckoutSerializer
from user.authentication import verify_token
import uuid


class CheckoutAPIView(APIView):
    """
    Class for Order API for order
    """

    @verify_token
    def post(self, request, cid):
        """
        function for place order api
        """
        try:
            user = User.objects.get(id=request.user.id)
            cart = Order.objects.get(id=cid)
            book = Book.objects.get(book_name=cart.book_id)
            data = request.data
            serializer = CheckoutSerializer(data)
            address = serializer.data['shipping_address']
            order_id = uuid.uuid4()
            order = Order.objects.create(user_id=user,
                                         book_id=book,
                                         order_id=order_id,
                                         shipping_address=address,
                                         quantity=cart.quantity,
                                         total_price=cart.total_price)
            order.status = OrderStatus.o.value
            order.save()
            cart.delete()
            return Response({'success': True,
                             'message': "Successfully Placed Order",
                             'data': f"Order Address- {address}, Order Id- {order_id}"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            Response({'success': False,
                      'message': "Something went wrong",
                      'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AddRatingsAPIView(APIView):
    """
    Class for Add Rating API for order
    """

    @verify_token
    def post(self, request, bid):
        """
        function for add rating api
        """
        try:
            query = f'SELECT * FROM book_book WHERE id={bid}'
            for queryset in Book.objects.raw(query):
                print(queryset)
                print(queryset.id)
                data = request.data
                queryset.ratings = data.get('ratings')
                queryset.save()
            return Response({'success': True,
                             'message': "Successfully added ratings"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)
