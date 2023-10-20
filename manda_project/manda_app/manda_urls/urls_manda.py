from django.urls import path
from ..manda_views import views_mandas

urlpatterns = [
    path('create/', views_mandas.manda_main_create, name='create'), 
]