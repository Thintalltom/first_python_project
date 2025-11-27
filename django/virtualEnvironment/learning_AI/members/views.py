from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


@swagger_auto_schema(
    methods=['post'], 
    request_body=UserSerializer,
    responses={201: UserSerializer, 200: UserSerializer(many=True)}
)
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    methods=['post'], 
    request_body=ProductSerializer,
    responses={201: ProductSerializer, 200: ProductSerializer(many=True)}
)
@api_view(['GET', 'POST'])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
