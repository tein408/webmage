from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..models import MandaMain, MandaSub, MandaContent
from ..serializers.manda_serializer import MandaMainSerializer, MandaSubUpdateSerializer, manda_sub_update_schema
import json

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(method='post', request_body=MandaMainSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def manda_main_create(request):
    user = request.user
    serializer = MandaMainSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
{
  "subs": [
    {"id": 1, "value": "new_value1"},
    {"id": 2, "value": "new_value2"},
    ...
    {"id": 8, "value": "new_value8"}
  ]
}
"""
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "subs": manda_sub_update_schema
        },
        required=["subs"]
    )
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_manda_subs(request):
    user = request.user
    data = request.data

    serializer = MandaSubUpdateSerializer(data=data.get('subs', []), many=True)

    if serializer.is_valid():
        for sub_data in serializer.validated_data:
            sub_id = sub_data.get('id')
            new_value = sub_data.get('sub_title')

            try:
                manda_sub = MandaSub.objects.get(id=sub_id, main_id__user=user)
            except MandaSub.DoesNotExist:
                return Response(f"MandaSub with ID {sub_id} does not exist for the current user.", status=status.HTTP_404_NOT_FOUND)

            manda_sub.sub_title = new_value
            manda_sub.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
