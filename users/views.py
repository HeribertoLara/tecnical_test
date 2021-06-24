from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serialized import UserSerializer


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        seriallized = UserSerializer(users, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=seriallized.data)

    def post(self,request):
        serialized= UserSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )
        serialized.save()
        return Response(status=status.HTTP_201_CREATED)
