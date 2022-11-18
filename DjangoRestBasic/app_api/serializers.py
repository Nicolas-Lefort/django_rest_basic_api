from rest_framework import serializers
from .models import Product, Supplier, ProductType

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
      model = Supplier
      fields = ('id', 'name', 'adress')

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
      model = ProductType
      fields = ('id', 'type')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
        "id",
        "type", 
        "supplier", 
        "reference",
        "cost",
        "stock_qty"
        ]