import json
from PIL import Image
from io import BytesIO
from users.models import EvUser
from aws.models import AWSDocument
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APITestCase
from rest_framework import status


class LogInTest(TestCase):
    redirect_url = '/'

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        EvUser.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertRedirects(response=response, expected_url=self.redirect_url)


class RegistrationTest(TestCase):
    redirect_url = '/'

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
        self.assertRedirects(response=response, expected_url=self.redirect_url)

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
        self.assertRedirects(response=response, expected_url=self.redirect_url)


class RetrieveUserInfoTest(APITestCase):
    user_url = '/api/user/'

    def setUp(self):
        self.user = EvUser.objects.create_user(username="test",
                                               password='test_password123',
                                               email="test@mail.it",
                                               is_organizer=False,
                                               profile_image=None)
        self.organizer = EvUser.objects.create_user(username="test_org",
                                                    organization_name="org",
                                                    password='test_password123',
                                                    email="test_org@mail.it",
                                                    is_organizer=True,
                                                    profile_image=None)

    def test_retrieve_user_main_info(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.user_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            {"username": "test",
             "organization_name": "",
             "is_organizer": False,
             "profile_image": None})

    def test_retrieve_organizer_main_info(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.get(self.user_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            {"username": "test_org",
             "organization_name": "org",
             "is_organizer": True,
             "profile_image": None, })


class UploadFileTest(APITestCase):
    def setUp(self):
        self.url = "/api/user/profile-image/"
        valid_file = SimpleUploadedFile("file.jpg", self.generate_mock_image().getvalue())
        invalid_file = SimpleUploadedFile("file.txt", self.generate_mock_image().getvalue())
        self.user = EvUser.objects.create_user(username="test",
                                               password='test_password123',
                                               email="test@mail.it",
                                               is_organizer=False,
                                               profile_image=None)
        self.data = {
            "profile_image.type": "PI",
            "profile_image.document": valid_file,
            "profile_image.loaded_by": self.user.id
        }

        self.none_image_data = {
            "profile_image.type": "PI",
            "profile_image.document": "",
            "profile_image.loaded_by": self.user.id
        }

        self.invalid_data = {
            "profile_image.type": "PI",
            "profile_image.document": invalid_file,
            "profile_image.loaded_by": self.user.id
        }

    def generate_mock_image(self):
        # generate mock file
        stream = BytesIO()
        image = Image.new('RGB', (100, 100))
        image.save(stream, format='jpeg')
        return stream

    def test_profile_image_upload_user_not_authenticated(self):
        response = self.client.put(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_set_none_image(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.url, self.none_image_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.profile_image, None)

    def test_profile_image_upload(self):
        # force login
        self.client.force_authenticate(user=self.user)

        response = self.client.put(self.url, self.data, format='multipart')
        aws_document = AWSDocument.objects.first()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.profile_image, aws_document)
        self.assertEqual(aws_document.loaded_by, self.user)

    def test_upload_invalid_format_file(self):
        # force login
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.url, self.invalid_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateUserProfileTest(APITestCase):
    def setUp(self):
        self.user = EvUser.objects.create_user(username="test",
                                               password='test_password123',
                                               email="test@mail.it",
                                               is_organizer=False,
                                               profile_image=None)

    def test_profile_detail_retrieve(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('user-profile', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'test')
