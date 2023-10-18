from rest_framework import status, generics
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ..serializers.user_serializer import UserSerializer

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            username = data['username']
            password = data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)
        except KeyError:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)