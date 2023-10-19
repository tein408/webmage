from django.shortcuts import redirect, render
from ..forms import FeedForm  # 게시글 폼을 사용하기 위해 필요한 import

# 글쓰기
def write(request):
    if request.method == 'POST':
        form = FeedForm(request.POST, request.FILES)  # 게시글 폼으로부터 데이터 받기

        if form.is_valid():
            # 폼이 유효하면 데이터베이스에 게시글 저장
            new_feed = form.save(commit=False)
            new_feed.user = request.user  # 현재 로그인한 사용자를 게시글 작성자로 설정
            new_feed.save()

            return redirect('feed_list')  # 게시글 목록 페이지로 리다이렉트

    else:
        form = FeedForm()

    return render(request, 'write.html', {'form': form})