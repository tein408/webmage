from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..models import MandaMain, MandaSub, MandaContent
from ..serializers.manda_serializer import MandaMainSerializer

from drf_yasg.utils import swagger_auto_schema

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def manda_main_create(request):
    user = request.user
    serializer = MandaMainSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)