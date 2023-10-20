from rest_framework import status
from django.contrib.auth.models import User
from ..models import MandaMain, MandaSub, MandaContent
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes

from drf_yasg.utils import swagger_auto_schema

@api_view(['POST'])
def manda_main_create(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)

        try:
            title = request.data['title']

            if len(title) > 100:
                return Response({'message': 'Title is too long!'}, status=status.HTTP_400_BAD_REQUEST)
            elif len(title) == 0 or title == '':
                return Response({'message': 'Please write title.'}, status=status.HTTP_400_BAD_REQUEST)
            
            MandaMain.objects.create(user=user, main_title=title, success=False)
        except KeyError:
            return Response({'message': 'Please write title.'}, status=status.HTTP_400_BAD_REQUEST)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)