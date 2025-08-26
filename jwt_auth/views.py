from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from django.contrib.auth.models import User
from jwt_auth.serializers import EmployeeSerializer,UserSerializer
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken


# class TokenAuthenticationView(APIView):
#     def post(self,request):
#         data=request.data
#         serializer=UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
#         user_data=User.objects.get(username=data['username'])
#         token_obj, _=Token.objects.get_or_create(user=user_data)

#         return Response({"Employee":data['username'],"token":str(token_obj)},status=200)
#     def get(self,request):
#         data=User.objects.all()
#         serializer=UserSerializer(data,many=True)
#         return Response({"message":serializer.data})


class RegistrationView(APIView):
    def post(self,request):
        data=request.data
        serializer=EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"error":serializer.errors},status=400)
        return Response({"message":"Employee Registered"},status=200)



class LoginView(APIView):
    def post(self,request):
        data=request.data 
        user=Employee.objects.get(emp_id=data['emp_id'])
        if not user:
            return Response({"error":f"{data['emp_id']} Does not exist"},status=404)
        if user and data['password']==user.password:
            return Response({"Emp_id":f"{data['emp_id']}","access_token":str(AccessToken.for_user(user)),"refresh_token":str(RefreshToken.for_user(user))},status=200)
        
class UserData(APIView):
    def get(self,request,emp_id):
        user_data=Employee.objects.get(emp_id=emp_id)
        serializer=EmployeeSerializer(user_data)
        print(serializer.data)
        return Response(serializer.data)

