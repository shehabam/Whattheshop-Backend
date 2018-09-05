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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # user_img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


# It creates a new Profile and associate it with the newly created User.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)
