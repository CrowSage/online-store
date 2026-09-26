from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully!"}, status=201)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
