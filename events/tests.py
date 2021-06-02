import json
from PIL import Image
from io import BytesIO

from aws.models import AWSDocument
from events.models import Category, Event
from users.models import EvUser
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APITestCase
from rest_framework import status


class EventManagingTest(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(EventManagingTest, cls).setUpClass()
        Category.objects.bulk_create(
            [Category(category="Art & Culture"),
             Category(category="Food"),
             Category(category="Sport"),
             Category(category="Music"),
             Category(category="Other")]
        )

        cls.user = EvUser.objects.create_user(username="test",
                                              password='test_password123',
                                              email="test@mail.it",
                                              is_organizer=False,
                                              profile_image=None)

        cls.organizer = EvUser.objects.create_user(username="test_org",
                                                   organization_name="org",
                                                   password='test_password123',
                                                   email="test_org@mail.it",
                                                   is_organizer=True,
                                                   profile_image=None)

    def test_categories_retrieve(self):
        url = reverse('categories')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         [{"id": 1, "category": "Art & Culture"},
                          {"id": 2, "category": "Food"},
                          {"id": 3, "category": "Sport"},
                          {"id": 4, "category": "Music"},
                          {"id": 5, "category": "Other"}])

    def test_create_event_not_organizer(self):
        url = '/api/events/'
        test_event = {
            "name": "test event",
            "description": "test description",
            "status": "S",
            "venue": "Test Venue",
            "start_date": "",
            "finish_date": "",
            "start_hour": "",
            "finish_hour": "",
            "evs_link": "",
            "event_website": "",
            "tickets_website": "",
            "organizer": self.user.id,
            "categories": [1, 2, 3, 4, 5]
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, test_event)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_event_organizer(self):
        url = '/api/events/'
        test_event = {
            "name": "test event",
            "description": "test description",
            "status": "S",
            "venue": "Test Venue",
            "start_date": "",
            "finish_date": "",
            "start_hour": "",
            "finish_hour": "",
            "evs_link": "",
            "event_website": "",
            "tickets_website": "",
            "organizer": self.organizer.id,
            "categories": [1, 2, 3, 4, 5]
        }
        self.client.force_authenticate(user=self.organizer)
        response = self.client.post(url, test_event)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_single_vent(self):
        test_event = Event.objects.create(
            name="Test event 2",
            description="Fixed description",
            status="A",
            organizer=self.organizer,
        )
        test_event.categories.add(Category.objects.get(id=1))
        url = '/api/events/{}/'.format(test_event.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['id'], test_event.id)
        self.assertEqual(json.loads(response.content)['name'], test_event.name)
        self.assertIn(test_event.categories.get(id=1).id, json.loads(response.content)['categories'])


class EventImageUploadTest(APITestCase):
    def setUp(self):
        valid_file = SimpleUploadedFile("file.jpg", self.generate_mock_image().getvalue())
        invalid_file = SimpleUploadedFile("file.txt", b'this is some text - not an image')

        self.organizer = EvUser.objects.create_user(username="test_org",
                                                    organization_name="org",
                                                    password='test_password123',
                                                    email="test_org@mail.it",
                                                    is_organizer=True,
                                                    profile_image=None)
        self.test_event = Event.objects.create(
            name="Test event 2",
            description="Fixed description",
            status="A",
            organizer=self.organizer,
        )

        self.valid_image_data = {
            "event_image.document": valid_file,
            "event_image.event": self.test_event.id,
            "event_image.loaded_by": self.organizer.id
        }

        self.none_image_data = {
            "event_image.document": "",
            "event_image.event": self.test_event.id,
            "event_image.loaded_by": self.organizer.id
        }

        self.invalid_data = {
            "event_image.document": invalid_file,
            "event_image.event": self.test_event.id,
            "event_image.loaded_by": self.organizer.id
        }
        self.url = "/api/events/{}/image/".format(self.test_event.id)

    def generate_mock_image(self):
        # generate mock file
        stream = BytesIO()
        image = Image.new('RGB', (100, 100))
        image.save(stream, format='jpeg')
        return stream

    def test_event_image_upload(self):
        # force login
        self.client.force_authenticate(user=self.organizer)

        response = self.client.put(self.url, self.valid_image_data, format='multipart')
        aws_document = AWSDocument.objects.first()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.first().event_image, aws_document)

    def test_set_none_event_image(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.put(self.url, self.none_image_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.first().event_image, None)

    def test_set_invalid_event_image_format(self):
        # force login
        self.client.force_authenticate(user=self.organizer)
        response = self.client.put(self.url, self.invalid_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
