from .models import register
from rest_framework import serializers

class RegisterSerializrs(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=255)
    mobile_no = serializers.IntegerField()
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return register.objects.create(**validated_data)
    
    
class LoginSerializrs(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=255)
    
    