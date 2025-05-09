from rest_framework import serializers
from myapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = "__all__"
        # fields =["name","email"]
        # exclude = ["name"]


class BookSerialize(serializers.ModelSerializer):
    class Meta :
        model = Book
        fields="__all__"