from django.urls import path
from ..manda_views import views_chat

urlpatterns = [
    path('rooms/', views_chat.get_rooms, name='rooms'), 
    path('current/<int:room_number>/<int:sender_id>', views_chat.chat_history, name='current'), 
]