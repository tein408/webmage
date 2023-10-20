from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import MandaMain, MandaSub, MandaContent
from ..serializers.manda_serializer import MandaMainSerializer
from django.urls import reverse

class MandaMainCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('create')

    def test_manda_main_create(self):
        data = {
            'user': self.user.id,
            'success': True,
            'main_title': 'Test Main Title'
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(MandaMain.objects.filter(user=self.user, main_title='Test Main Title').exists())

        created_object = MandaMain.objects.get(user=self.user, main_title='Test Main Title')
        expected_data = MandaMainSerializer(created_object).data
        self.assertEqual(response.data, expected_data)

    def test_unauthenticated_user(self):
        self.client.logout()
        data = {'title': 'Test Title'}
        
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_manda_main_title_too_long(self):
        self.client.login(username='testuser', password='testpassword')
        long_title = 'a' * 101
        data = {'title': long_title}

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('main_title', response.data)

    def test_invalid_manda_main_title(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('main_title', response.data)

class MandaMainSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('create')

    def test_main_title_length_validation(self):
        too_long_title = 'a' * 101
        empty_title = ''

        too_long_data = {
            'user': self.user.id,
            'success': True,
            'main_title': too_long_title
        }
        empty_data = {
            'user': self.user.id,
            'success': True,
            'main_title': empty_title
        }

        serializer1 = MandaMainSerializer(data=too_long_data)
        serializer2 = MandaMainSerializer(data=empty_data)

        self.assertFalse(serializer1.is_valid())
        self.assertFalse(serializer2.is_valid())

        self.assertIn('title은 100자 이하여야 합니다.', serializer1.errors['main_title'][0])
        self.assertIn('This field may not be blank.', serializer2.errors['main_title'][0])