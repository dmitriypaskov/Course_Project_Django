from django.db import models
from django.utils import timezone

from order.models import Order, Delivery
from user.models import Employee, User


class Category(models.Model):
    name = models.CharField(max_length=255)


class FetchSpecification(models.Model):
    size = models.CharField(max_length=255)
    weight = models.FloatField()
    color = models.CharField(max_length=255)
    description = models.TextField()


class WrittenOff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    fetch_specification = models.ForeignKey(FetchSpecification, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order, blank=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    exploitation_term = models.IntegerField()


class ProductUnit(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    written_off = models.OneToOneField(WrittenOff, on_delete=models.CASCADE)
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)











