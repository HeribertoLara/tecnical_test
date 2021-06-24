from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from addresses.models import Address
from addresses.serializers import AdressSerializer


class AdressView(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        seriallizer = AdressSerializer(addresses, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=seriallizer.data)

