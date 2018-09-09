from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import RegisterSerializer, ItemSerializer
from .models import Product, Order, MiddleMan
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


# SHOWING THE LIST


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = .....


class MakingOrders(APIView):
    def post(self, request, *args, **kwargs):
        order_obj = Order.objects.create(user=request.user)
        for order in request.data.get("data"):
            product_id = order.get("id")
            quantity = order.get("quantity")
            product_obj = Product.objects.get(id=product_id)
            middleMan = MiddleMan.objects.create(
                quantity=quantity, order=order_obj, product=product_obj)
        return Response(status=status.HTTP_201_CREATED)


# EDDITING A USER PROFILE
# class ...(APIView):
#     def put(self, request):
#         profile = request.user.profile
#         data = request.data
#         serializer_class = ProfileSerializer(profile, data=data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer_class.data, status=status.HTTP_400_BAD_REQUEST)
