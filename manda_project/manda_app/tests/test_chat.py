from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from ..models import ChatRoom, ChatMessage, UserProfile

class GetRoomsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('rooms')

    def test_get_rooms(self):
        chat_room1 = ChatRoom.objects.create(starter=self.user)
        chat_room2 = ChatRoom.objects.create(starter=self.user2, receiver=self.user)

        ChatMessage.objects.create(chatroom=chat_room1, content='Hello', author=self.user)
        ChatMessage.objects.create(chatroom=chat_room2, content='Hi', author=self.user2)

        response = self.client.get(self.url)
        rooms_data = response.data.get('rooms')

        # 내가 속한 채팅방 수 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(rooms_data)
        self.assertEqual(len(rooms_data), 2)

        # 로그인 한 유저가 starter 인 경우
        first_room_data = rooms_data[0]
        self.assertEqual(first_room_data['chat_room_id'], chat_room1.pk)
        self.assertEqual(first_room_data['starter_id'], self.user.pk)
        self.assertEqual(first_room_data['starter'], self.user.username)
        self.assertEqual(first_room_data['message'], 'Hello')
        self.assertEqual(first_room_data['unread_message_count'], 0) 

        # 로그인 한 유저에게 채팅이 온 경우
        second_room_data = rooms_data[1]
        self.assertEqual(second_room_data['chat_room_id'], chat_room2.pk)
        self.assertEqual(second_room_data['starter_id'], self.user.pk)
        self.assertEqual(second_room_data['starter'], self.user.username)
        self.assertEqual(second_room_data['message'], 'Hi')
        self.assertEqual(second_room_data['unread_message_count'], 1)

