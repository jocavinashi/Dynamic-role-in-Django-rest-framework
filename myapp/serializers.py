from rest_framework import serializers
# from .models import Role
from django.contrib.auth.models import Permission
from . import models

class RoleSerializer(serializers.ModelSerializer):
    # groups = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True)
    # permission= serializers.CharField(read_only=True)
    class Meta:
        model=models.Role
        fields=['id','role','groups']

class UserSerializer(serializers.ModelSerializer):
    role_name=serializers.CharField(source='role.role',read_only=True)
    class Meta:
        model=models.User
        fields=['id','email','name','created','is_active','role','role_name']