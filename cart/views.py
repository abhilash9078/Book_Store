from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
import logging
from order.models import Order
from cart.serializers import CartSerializer, GetCartSerializer, EditCartSerializer
from user.authentication import verify_token
from drf_yasg.utils import swagger_auto_schema


logger = logging.getLogger('django')


class CartAPIView(GenericAPIView):
    """
    class view for performing crud operation with cart
    """
    serializer_class = CartSerializer

    @swagger_auto_schema(request_body=CartSerializer)
    @verify_token
    def post(self, request):
        """
        post function for post request for adding books to cart
        """
        try:
            serializer = CartSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info("Successfully added into cart")
            return Response({'success': True,
                             'message': "Successfully added in cart",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': str(e),
                             'data': {}}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def get(self, request):
        """
        get function for get request to view all cart item
        """
        try:
            cart = Order.objects.filter(user_id=request.user)
            serializer = GetCartSerializer(instance=cart, many=True)
            logger.info("view cart item")
            return Response({'success': True,
                             'message': "Cart Items",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self, request, id):
        """
        delete function for delete request to delete item from cart
        """
        try:
            cart = Order.objects.get(id=id)
            cart.delete()
            logger.info("successfully deleted")
            return Response({'success': True,
                             'message': "Successfully deleted "}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=EditCartSerializer)
    @verify_token
    def patch(self, request, id):
        """
        patch function for patch request to update cart item
        """
        try:
            data = request.data
            serializer = EditCartSerializer(data=data)
            if serializer.is_valid():
                quantity = serializer.data['quantity']
                cart = Order.objects.get(id=id)
                if not cart:
                    logger.error("quantity is not available")
                    return Response({'success': False,
                                     'message': "Given cart item is not Available",
                                     'data': id},
                                    status=status.HTTP_404_NOT_FOUND)
                cart.quantity = quantity
                cart.total_price = cart.book_id.price * quantity
                cart.save()
                logger.info("Successfully edited the cart item")
                return Response({'success': True,
                                 'message': "Successfully Edited the cart item "}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)
