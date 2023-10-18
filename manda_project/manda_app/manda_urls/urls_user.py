from django.urls import path
from django.contrib.auth import views as auth_views
from ..manda_views import views_users

urlpatterns = [
    path('login/', views_users.user_login, name='login'), 
    path('logout/', views_users.user_logout, name='logout'), 
    path('signup/', views_users.sign_up, name='signup'), 
    path('edit/', views_users.user_edit, name='edit'),
]