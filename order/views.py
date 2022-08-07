from rest_framework import status
from rest_framework.views import APIView, Response
from cart.models import Cart
from user.models import User
from book.models import Book
from .models import Order
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
            cart = Cart.objects.get(id=cid)
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
            order.save()
            book.save()
            cart.delete()
            return Response({'success': True,
                             'message': "Successfully Placed Order",
                             'data': f"Order Address- {address}, Order Id- {order_id}"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            Response({'success': False,
                      'message': "Something went wrong",
                      'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)
