# from rest_framework.serializers import Serializer
from rest_framework import serializers
from .models import product

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields= ['name', 'price',]

class HumanSerializer(serializers.ModelSerializer):
    pass    