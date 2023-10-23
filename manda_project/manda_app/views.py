from django.shortcuts import render
from django.http import JsonResponse
from .models import Feed
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view


# Create your views here.
def main(request):
    return render(request, 'main.html')

def feed_list_view(request):
    feeds = Feed.objects.all()
    data = [{'id': feed.id, 'feed_contents': feed.feed_contents} for feed in feeds]
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})