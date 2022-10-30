from itertools import product
from math import prod
from django.shortcuts import render;
from django.shortcuts import get_object_or_404;
from rest_framework import status;
from rest_framework.response import Response;
from rest_framework.permissions import IsAuthenticated, AllowAny;
from rest_framework.decorators import api_view, permission_classes;
from rest_framework.permissions import IsAdminUser;
from .models import Product;
from .serializers import ProductSerializer;
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger;



@api_view(['GET', 'POST'])
@permission_classes([AllowAny])     
def inventory_list(request):
    if request.method == 'GET':
        product_param = request.query_params.get('_id')
        sort_param = request.query_params.get('sort')
        product = Product.objects.all()
        if product_param:
            product = product.filter(_id=product_param)
        elif sort_param:
            product = product.order_by(sort_param)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):

    user = request.user
    product = Product.objects.create(
        user = user,
        name = " Product Name ",
        price = 0,
        brand = "Sample brand ",
        # countInStock = 0,
        # category="Sample category",
        description = " "
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

# Update single products


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)

    product.name = data["name"]
    product.price = data["price"]
    product.brand = data["brand"]
    # product.countInStock = data["countInStock"]
    # product.category = data["category"]
    product.description = data["description"]

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


# Delete a product
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response("Product deleted successfully")


# Upload Image
@api_view(['POST'])
def uploadImage(request):
    data = request.data
    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)
    product.image = request.FILES.get('image')
    product.save()
    return Response("Image was uploaded")