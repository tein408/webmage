from django.shortcuts import redirect, render
from ..forms import FeedForm  # 게시글 폼을 사용하기 위해 필요한 import
from ..models import Feed
from ..serializers import FeedSerializer

# 글쓰기
class FeedCreateView(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer