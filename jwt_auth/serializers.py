from rest_framework import serializers
# from jwt_auth import views
from .models import Employee
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['username','password','email']
