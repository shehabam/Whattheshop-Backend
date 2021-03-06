from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Order, MiddleMan, Category
from rest_framework_jwt.settings import api_settings


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token', ]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token
        return validated_data

# LIST SERIALIZER

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'img', 'price', 'id']

class CategorySerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

    def get_items(self, obj):
        items = obj.product_set.all()
        return ItemSerializer(items, many=True).data




class MiddleManSerializer(serializers.ModelSerializer):
    product = ItemSerializer()
    class Meta:
        model = MiddleMan
        fields = ['quantity', 'product']

class OrderListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    middleman_set = MiddleManSerializer(many=True)

    class Meta:
        model = Order
        exclude = ['products']
