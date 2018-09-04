from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import RegisterSerializer, ItemSerializer, ItemDetailSerializer
from .models import Product


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

# SHOWING THE LIST


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = .....


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
