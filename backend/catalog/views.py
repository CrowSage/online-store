from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Product


# RETURN ALL PRODUCTS (OR CATERGORY WITH QUERY PARAM)
@api_view(["GET"])
@permission_classes([AllowAny])
def product_list(request):
    pass


# RETURN DETAILS OF A SINGLE PRODUCT
@api_view(["GET"])
@permission_classes([AllowAny])
def product_detail(request, pk):

    pass
