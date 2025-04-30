from rest_framework import serializers
from django import forms
from .models import Todo, User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','username','password']


    def create(self, validated_data):
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields="__all__"
