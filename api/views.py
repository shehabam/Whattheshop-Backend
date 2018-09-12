from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import RegisterSerializer, CategorySerializer, OrderListSerializer
from .models import Product, Order, MiddleMan, Category
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

#REGISTERING
class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


# SHOWING THE LIST


class ProductListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = .....

#ACCEPTING THE ORDER FROM THE FRONTEND
class MakingOrders(APIView):
    def post(self, request, *args, **kwargs):
        order_obj = Order.objects.create(user=request.user)
        for order in request.data:
            product_id = order.get("id")
            quantity = order.get("quantity")
            product_obj = Product.objects.get(id=product_id)
            middleMan = MiddleMan.objects.create(
                quantity=quantity, order=order_obj, product=product_obj)
        return Response(status=status.HTTP_201_CREATED)

#USERS ORDER LIST
class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class UserOrder(APIView):
    # queryset = Order.objects.all()
    # serializer_class = OrderListSerializer
    # lookup_field = 'user'
    # lookup_url_kwarg = 'user_id'

    def get(self, request, *args, **kwargs):
        user_orders = Order.objects.filter(user=request.user.id)
        serializer = OrderListSerializer(user_orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
