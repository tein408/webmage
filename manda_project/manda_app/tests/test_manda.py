from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from ..models import MandaMain, MandaSub, MandaContent
from django.urls import reverse

class MandaMainCreateTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('create')

    def test_manda_main_create(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Test Title'}
        
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(MandaMain.objects.filter(user=self.user, main_title='Test Title', success=False).exists())

    def test_unauthenticated_user(self):
        self.client.logout()
        data = {'title': 'Test Title'}
        
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_manda_main_title_too_long(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901'}

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Title is too long!')

    def test_manda_main_title_length_zero(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': ''}

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Please write title.')

    def test_invalid_manda_main_title(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Please write title.')