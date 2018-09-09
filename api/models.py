from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_of_purchase = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, through='MiddleMan')


class MiddleMan(models.Model):
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


# It creates a new Profile and associate it with the newly created User.
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile(sender, instance=None, created=False, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# order_obj = Order.objects.create(user=request.user)

# order_list = request.data.get("data")
# for order in order_list:
#     product_id = order.get("id")
#     quantity = order.get("quantity")
#     product_obj = Product.objects.get(id=product_id)
#     middleman = MiddleMan.objects.create(product=product_obj, quantity=quantity, order=)


# return Response(status=status.HTTP_201_CREATED)
