# flake8: noqa
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializers import *


class HelloAuthView(GenericAPIView):

    def get(self, request):
        return Response(data={"message": "Hellow Auth"}, status=HTTP_200_OK)


class UserSerializer(GenericAPIView):
    serializer_class = UserCreationSerializer

    @swagger_auto_schema(operation_summary="Create a user account by signing Up")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
