from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import RegisterSerializer, ItemSerializer
from .models import Product, Profile
from rest_framework import status
from rest_framework.response import Response


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


# SHOWING THE LIST


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = .....

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
