from rest_framework import serializers
from library.models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

    def validate(self, data):
        
        if data['age']<18:
            raise serializers.ValidationError("age must be above 18")
        return data
    

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publication
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        depth=1
    
    # def to_representation(self, instance): 

    #     resp = super().to_representation(instance)
    #     resp['author'] = AuthorSerializer(instance.author).data
    #     resp['publication'] = PublicationSerializer(instance.publication).data
    #     return resp

      
       

    
    