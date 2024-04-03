from django.db import models
from django.utils import timezone

from products.models import ProductUnit


class Access_Management(models.Model):
    is_super_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    creation_rights = models.BooleanField(default=False)
    deletion_rights = models.BooleanField(default=False)
    modification_rights = models.BooleanField(default=False)
    read_rights = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)


class Employee(models.Model):
    products_unit = models. ManyToManyField(ProductUnit)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date = models.DateTimeField(default=timezone.now)


class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    access_management = models.OneToOneField(Access_Management, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)









