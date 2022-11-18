from django.db import models
#from django.contrib.auth.models import User

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class Product(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    reference = models.TextField(null=True, blank=True)
    cost = models.FloatField(default=10.0)
    stock_qty = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.reference
