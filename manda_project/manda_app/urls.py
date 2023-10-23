from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from manda_app.views import TestView

from .manda_urls.urls_user import urlpatterns as manda_user_urls
from .manda_urls.urls_write import urlpatterns as manda_app_write_urls

urlpatterns = [
    path('v1/test/', TestView.as_view(), name='test'),
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('user/', include(manda_user_urls)), #회원가입, 로그인, 로그아웃 url
    path('write/', include(manda_app_write_urls)), #글 작성, 글 선택
]