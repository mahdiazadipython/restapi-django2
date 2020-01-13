from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Product
from.serializers import ProductSerializers
from rest_framework import status




@api_view(["GET","POST"])
def product_list(request):
    if request.method == "GET":
        obj = Product.objects.all()
        serializer  = ProductSerializers(obj,many = True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer = ProductSerializers(data  = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(["GET","PUT"])
def detail(request,pk):
    try:
        obj = Product.objects.get(id =pk)
    except Product.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":               
        serializer = ProductSerializers(obj)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer=ProductSerializers(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    
    