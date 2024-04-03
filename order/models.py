

from django.db import models
from django.utils import timezone

from products.models import Product, ProductUnit
from user.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models. ManyToManyField(Product)
    date = models.DateTimeField(default=timezone.now)


class Delivery(models.Model):
    product_unit = models. ManyToManyField(ProductUnit)
    date = models.DateTimeField(default=timezone.now)
    responsiveness_to_order = models.BooleanField(default=True)
    descriptions_responsiveness_to_order = models.TextField()
    responsiveness_to_delivery = models.BooleanField(default=True)




