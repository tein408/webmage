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
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('rooms')

    def test_get_rooms(self):
        chat_room1 = ChatRoom.objects.create(starter=self.user)
        chat_room2 = ChatRoom.objects.create(receiver=self.user)
        ChatMessage.objects.create(chat_room=chat_room1, content='Hello', author=self.user)
        ChatMessage.objects.create(chat_room=chat_room2, content='Hi', author=self.user)

        response = self.client.post(self.url, format='json')

        rooms_data = response.data
        first_room_data = rooms_data[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(rooms_data), 2)
        self.assertEqual(first_room_data['chat_room_id'], chat_room1.pk)
        self.assertEqual(first_room_data['starter_id'], self.user.pk)
        self.assertEqual(first_room_data['starter'], self.user.username)
        self.assertEqual(first_room_data['message'], 'Hello')

