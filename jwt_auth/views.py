from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from django.contrib.auth.models import User
from jwt_auth.serializers import EmployeeSerializer,UserSerializer


class TokenAuthenticationView(APIView):
    def post(self,request):
        data=request.data
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
        user_data=User.objects.get(username=data['username'])
        token_obj, _=Token.objects.get_or_create(user=user_data)

        return Response({"Employee":data['username'],"token":str(token_obj)},status=200)
    def get(self,request):
        data=User.objects.all()
        serializer=UserSerializer(data,many=True)
        return Response({"message":serializer.data})

