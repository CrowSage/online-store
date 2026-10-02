from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartViewSerializer


# For viewing your cart
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cart_view(request):

    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)

    serialzer = CartViewSerializer(cart)

    return Response(serialzer.data)
