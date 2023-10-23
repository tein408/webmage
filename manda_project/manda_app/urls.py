from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls.static import static

from .manda_urls.urls_user import urlpatterns as manda_user_urls
from .manda_urls.urls_write import urlpatterns as manda_write_urls
from .manda_urls.urls_manda import urlpatterns as manda_manda_urls

urlpatterns = [
    path('', views.main, name='main'),
    path('user/', include(manda_user_urls)), #회원가입, 로그인, 로그아웃 url
    path('write/', include(manda_write_urls)), #글 작성, 글 선택
    path('manda/', include(manda_manda_urls)), #만다라트
    path('get_token/', views.get_csrf_token, name='get_token'),
]