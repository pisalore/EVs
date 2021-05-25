from users.models import EvUser
from django.test import TestCase


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
