from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework import status
from .models import Todo
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer, UserRegistrationSerializer

# Create your views here.


class UserRegisterView(APIView):
    def post(self,request):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"User registered successfully!"
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class UserTodoListView(APIView):
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        todos=Todo.objects.filter(user=request.user)
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
