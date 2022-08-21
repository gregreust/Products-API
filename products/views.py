from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductsSerializer
from .models import Products

# Create your views here.

@api_view(['GET', 'POST'])
def products_list(request):

    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        # if serializer.is_valid() == True:  
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #vvv same function as above, with less code vvv
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def product_byid(request, pk):
    try:
        product = Products.objects.get(id=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
        
    except Products.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


    