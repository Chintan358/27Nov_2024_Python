from rest_framework import serializers
from myapp.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields="__all__"