import json

from users.models import EvUser
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        EvUser.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)


class RegistrationTest(TestCase):
    def test_user_registration(self):
        url = '/accounts/register/user/'
        user_data = {
            'first_name': 'test',
            'last_name': 'user',
            'birthday': '1995-04-13',
            'city': 'test_city',
            'username': 'test_username',
            'email': 'test@test.it',
            'password1': 'averystrongPassword123',
            'password2': 'averystrongPassword123'
        }

        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 302)

    def test_organizer_registration(self):
        url = '/accounts/register/organizer/'
        organizer_data = {
            'organization_name': 'test',
            'username': 'city_username',
            'email': 'test@organization.it',
            'password1': 'averystrongPassword123',
            'password2': 'averystrongPassword123'
        }

        response = self.client.post(url, organizer_data)
        self.assertEqual(response.status_code, 302)


class RetrieveUserInfoTest(APITestCase):
    user_url = '/api/user/'

    def setUp(self):
        self.user = EvUser.objects.create_user(username="test",
                                               password='test_password123',
                                               email="test@mail.it",
                                               is_organizer=False)
        self.organizer = EvUser.objects.create_user(username="test_org",
                                                    organization_name="org",
                                                    password='test_password123',
                                                    email="test_org@mail.it",
                                                    is_organizer=True)

    def test_retrieve_user_main_info(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.user_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            {"username": "test",
             "organization_name": "",
             "is_organizer": False})

    def test_retrieve_organizer_main_info(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.get(self.user_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            {"username": "test_org",
             "organization_name": "org",
             "is_organizer": True})
