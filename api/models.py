from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
