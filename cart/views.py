from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from book.models import Book
from order.models import Order
from cart.serializers import CartSerializer, GetCartSerializer, EditCartSerializer
from user.authentication import verify_token
from drf_yasg.utils import swagger_auto_schema


class CartAPIView(GenericAPIView):
    serializer_class = CartSerializer

    @swagger_auto_schema(request_body=CartSerializer)
    @verify_token
    def post(self, request):
        try:
            serializer = CartSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True,
                             'message': "Successfully added in cart",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': str(e),
                             'data': {}}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def get(self, request):
        try:
            cart = Order.objects.filter(user_id=request.user)
            serializer = GetCartSerializer(instance=cart, many=True)
            return Response({'success': True,
                             'message': "Cart Items",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self, request, id):
        try:
            cart = Order.objects.get(id=id)
            cart.delete()
            return Response({'success': True,
                             'message': "Successfully deleted "}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=EditCartSerializer)
    @verify_token
    def patch(self, request, id):
        try:
            data = request.data
            serializer = EditCartSerializer(data=data)
            if serializer.is_valid():
                quantity = serializer.data['quantity']
                cart = Order.objects.get(id=id)
                if not cart:
                    return Response({'success': False,
                                     'message': "Given cart item is not Available",
                                     'data': id},
                                    status=status.HTTP_404_NOT_FOUND)
                cart.quantity = quantity
                cart.total_price = cart.book_id.price * quantity
                cart.save()
                return Response({'success': True,
                                 'message': "Successfully Edited the cart item "}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)
