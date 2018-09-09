from django.urls import path
from .views import RegisterAPIView
from rest_framework_jwt.views import obtain_jwt_token
from api.views import ProductListAPIView, MakingOrders

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('list/', ProductListAPIView.as_view(), name='api-list'),
    path('orders/', MakingOrders.as_view(), name='api-order')

]
