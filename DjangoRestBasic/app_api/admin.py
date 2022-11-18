from django.contrib import admin

# Register your models here.
from .models import Supplier, ProductType, Product

admin.site.register(Supplier)
admin.site.register(ProductType)
admin.site.register(Product)