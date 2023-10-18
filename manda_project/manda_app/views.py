from django.shortcuts import render
from django.http import JsonResponse
from .models import Feed


# Create your views here.
def main(request):
    return render(request, 'main.html')

def feed_list_view(request):
    feeds = Feed.objects.all()
    data = [{'id': feed.id, 'feed_contents': feed.feed_contents} for feed in feeds]
    return JsonResponse(data, safe=False)