from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser, Todo
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed,NotAuthenticated
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer, UserSerializer
import jwt

from datetime import datetime,timedelta, timezone

# Create your views here.


class UserRegisterView(APIView):
    #register
    def post(self,request):
        password=request.data['password']
        email=request.data['email']
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            #return Response({
            #    "message":"User registered successfully!"
            #},status=status.HTTP_201_CREATED)
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    #login
    def get(self,request):
        email=request.data['email']
        password=request.data['password']

        user=CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("email is not registered")

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect email/password')

        payload={
            'id':user.id,
            'exp':datetime.now(timezone.utc)+timedelta(minutes=60),
            'iat':datetime.now(timezone.utc)
        }

        token=jwt.encode(payload,'asdsdaj7364638#h#723y8@#$',algorithm='HS256')
        response=Response()
        response.set_cookie(
            key="jwt",value=token,httponly=True
        )
        response.data={
            'data':user.email,
            'message':"Login Succesful!"
        }
        return response

class UserLogoutView(APIView):
    #logout
    def post(self,request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':"Logout Successful!"
        }
        return response




class UserTodoListView(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise NotAuthenticated("Unauthenticated!")
        payload=jwt.decode(token,'asdsdaj7364638#h#723y8@#$',algorithms=['HS256'])
        todos=Todo.objects.filter(user_id=payload['id'])
        serializer=TodoSerializer(todos,many=True)
        return Response({"data":serializer.data},status=status.HTTP_200_OK) 

    def post(self,request):
        new_task=TodoSerializer(request.data)
        if new_task.is_valid():
            new_task.save()
            return Response({"status":"success","data":new_task.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"Invalid Data","data":new_task.errors},status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,id=None):
        item=Todo.objects.get(id=id)
        serializer=TodoSerializer(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        else:
            return Response({"status":"error","data":serializer.errors})
        

    def delete(self,request,id=None):
        item=get_object_or_404(Todo,id=id)
        item.delete()
        return Response({"status":"success","data":f"{item.title}Todo Deleted"})


