from django.urls import path, include
from . import views

from .manda_urls.urls_user import urlpatterns as manda_user_urls

urlpatterns = [
    path('', views.main, name='main'),
    path('user/', include(manda_user_urls)), #회원가입, 로그인, 로그아웃 url
]