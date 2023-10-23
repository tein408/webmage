from django.shortcuts import render
from django.http import JsonResponse
from .models import Feed

from django.middleware.csrf import get_token
from rest_framework.decorators import api_view

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def main(request):
    return render(request, 'main.html')

def feed_list_view(request):
    feeds = Feed.objects.all()
    data = [{'id': feed.id, 'feed_contents': feed.feed_contents} for feed in feeds]
    return JsonResponse(data, safe=False)
  
class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response("Swagger 연동 테스트")

@api_view(['GET'])
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})
