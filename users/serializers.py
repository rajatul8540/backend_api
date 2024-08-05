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
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        instance.save()
        return instance
    
    
class LoginSerializrs(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=255)
    
    