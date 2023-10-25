from django.urls import path
from ..manda_views import views_chat

urlpatterns = [
    path('rooms/', views_chat.get_rooms, name='rooms'), 
]