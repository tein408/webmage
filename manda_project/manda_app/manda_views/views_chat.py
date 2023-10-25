from rest_framework import status
from django.utils import timezone
from ..models import ChatRoom, ChatMessage, UserProfile
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def format_datetime(dt):
    today = timezone.now().date()
    if dt.date() == today:
        return dt.strftime("오늘 %p %I:%M")
    yesterday = today - timezone.timedelta(days=1)
    if dt.date() == yesterday:
        return dt.strftime("어제 %p %I:%M")
    return dt.strftime("%Y-%m-%d %p %I:%M")

@api_view(['GET'])
def get_rooms(request):
    chat_rooms = ChatRoom.objects.filter(Q(starter=request.user.id) | Q(receiver=request.user.id))

    latest_messages = []

    for room in chat_rooms:
        try:
            unread_message_count = ChatMessage.objects.filter(
                Q(chatroom=room),
                ~Q(author=request.user),
                Q(is_read=False)
            ).count()

            latest_message = ChatMessage.objects.filter(chatroom=room).latest('created_at')
            starter = None

            if latest_message.chatroom.starter == request.user:
                starter = latest_message.chatroom.starter
            else:
                starter = latest_message.chatroom.receiver 

            latest_messages.append({
                'chat_room_id': room.pk,
                'starter_id': starter.pk,
                'starter': starter.username,
                'message': latest_message.content,
                'created_at': format_datetime(latest_message.created_at),
                'unread_message_count': unread_message_count,
            })
        except ChatMessage.DoesNotExist:
            starter = None

            if room.starter.pk == request.user.id:
                starter = User.objects.get(pk=request.user.id)
            else:
                starter = room.starter

            latest_messages.append({
                'chat_room_id': room.pk,
                'starter_id': starter.pk,
                'starter': starter.username,
                'message': '',
                'created_at': '',
                'unread_message_count': 0,
            })

    latest_messages.sort(key=lambda x: x['created_at'], reverse=True)

    return Response({'rooms':latest_messages}, status=status.HTTP_200_OK)

@api_view(['GET'])
def chat_history(request, room_number, sender_id):
    current_chat = None
    formatted_chat_msgs = []
    first_unread_index = -1

    current_room = ChatRoom.objects.get(pk=room_number)
    current_chat = ChatMessage.objects.filter(chatroom=current_room).order_by('created_at')

    for chat in current_chat:
        if chat.is_read == False:
            if chat.author.pk != request.user.id:
                chat.is_read = True
                chat.save()
                if first_unread_index == -1:
                    first_unread_index = chat.pk

    for chat in current_chat:
        formatted_chat_msgs.append({
            'created_at': format_datetime(chat.created_at),
            'message': chat.content,
            'username': chat.author.username,
            'is_read': chat.is_read, 
            'id': chat.pk,
        })

    sender_name = User.objects.get(pk=sender_id).username

    context = {
        "room_number" : room_number,
        "chat_msgs" : formatted_chat_msgs,
        'first_unread_index': first_unread_index,
        'sender': sender_name
    }

    return Response(context, status=status.HTTP_200_OK)