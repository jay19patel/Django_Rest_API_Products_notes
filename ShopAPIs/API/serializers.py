from rest_framework import serializers
from .models import Products

class MyProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','name','company','quantity','price','image','category','description']  
