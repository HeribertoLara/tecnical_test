from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serialized import UserSerializer#, AddressUserSerializer
#from addresses.serializers import AdressSerializer

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        seriallized = UserSerializer(users, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=seriallized.data)

    def post(self, request):
        serialized = UserSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )
        serialized.save()
        return Response(status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serialized = UserSerializer(user)
            return Response(status=status.HTTP_200_OK, data=serialized.data)



"""class UserAddressDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id).adress
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serialized = UserSerializer(user)
            return Response(status=status.HTTP_200_OK, data=serialized.data)"""

