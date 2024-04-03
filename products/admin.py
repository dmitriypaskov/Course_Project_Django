from django.contrib import admin

from products.models import Category, Fetch_Specification, Written_Off, Product, Product_Unit


admin.site.register(Category)
admin.site.register(Fetch_Specification)
admin.site.register(Written_Off)
admin.site.register(Product)
admin.site.register(Product_Unit)
