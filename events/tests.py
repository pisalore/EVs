import datetime
import json
from PIL import Image
from io import BytesIO

from aws.models import AWSDocument
from events.models import Category, Event
from users.models import EvUser
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APITestCase, APIClient
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
        self.client = APIClient()
        url = '/api/events/'
        test_event = {
            "name": "test event",
            "description": "test description",
            "status": "S",
            "venue": "Test Venue",
            "start_date": "2021-06-15",
            "finish_date": "2021-06-15",
            "start_hour": "15:29:58",
            "finish_hour": "15:29:58",
            "evs_link": "",
            "event_website": "",
            "tickets_website": "",
            "organizer": self.organizer.id,
            "categories": [
                {
                    "category": "Music",
                    "id": 1
                },
            ]
        }
        self.client.force_authenticate(user=self.organizer)
        response = self.client.post(url, test_event, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_single_event(self):
        test_event = Event.objects.create(
            name="Test event 2",
            description="Fixed description",
            status="A",
            organizer=self.organizer,
            start_date=datetime.date.today().__str__()
        )
        test_event.categories.add(Category.objects.get(id=1))
        url = '/api/events/{}/'.format(test_event.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['id'], test_event.id)
        self.assertEqual(json.loads(response.content)['name'], test_event.name)
        self.assertEqual(test_event.categories.get(id=1).category, "Art & Culture")

    def test_event_update(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.organizer)
        test_event = Event.objects.create(
            name="Test event 2",
            description="Fixed description",
            status="A",
            organizer=self.organizer,
            start_date=datetime.date.today().__str__(),
        )
        test_event.categories.add(Category.objects.get(id=1))
        update_event_data = {
            "name": "Test event renamed",
            "description": "test description",
            "status": "S",
            "venue": "Test Venue",
            "start_date": (datetime.date.today() + datetime.timedelta(days=1)).__str__(),
            "finish_date": (datetime.date.today() + datetime.timedelta(days=2)).__str__(),
            "start_hour": "15:29:58",
            "finish_hour": "15:29:58",
            "evs_link": "",
            "event_website": "",
            "tickets_website": "",
            "organizer": self.organizer.id,
            "categories": [
                {
                    "category": "Music",
                    "id": 1
                },
            ]
        }
        url = '/api/events/{}/'.format(test_event.id)
        response = self.client.put(url, update_event_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['name'], "Test event renamed")
        self.assertEqual(json.loads(response.content)['venue'], "Test Venue")

    def test_event_delete(self):
        self.client.force_authenticate(user=self.organizer)
        test_event = Event.objects.create(
            name="Test event 2",
            description="Fixed description",
            status="A",
            organizer=self.organizer,
            start_date=datetime.date.today().__str__()
        )
        url = '/api/events/{}/'.format(test_event.id)
        test_event.categories.add(Category.objects.get(id=1))
        self.client.delete(url)

        self.assertFalse(Event.objects.filter(pk=test_event.id).exists())


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


class FilterEventsTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(FilterEventsTest, cls).setUpClass()
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

        cls.organizer2 = EvUser.objects.create_user(username="test_org2",
                                                    organization_name="org2",
                                                    password='test_password123',
                                                    email="test_org2@mail.it",
                                                    is_organizer=True,
                                                    profile_image=None)

        cls.A1 = Event.objects.create(organizer=cls.organizer,
                                      name="TestEvent1A",
                                      status="A",
                                      start_date=datetime.date.today().__str__(),
                                      venue="TestVenue")

        cls.A2 = Event.objects.create(organizer=cls.organizer2,
                                      name="TestEvent2A",
                                      status="A",
                                      start_date=datetime.date.today().__str__(),
                                      venue="TestVenue")

        cls.A3 = Event.objects.create(organizer=cls.organizer2,
                                      name="TestEvent3A",
                                      status="A",
                                      start_date=datetime.date.today().__str__(),
                                      venue="TestVenue")

        cls.S = Event.objects.create(organizer=cls.organizer,
                                     name="TestEvent2S",
                                     status="S",
                                     start_date=datetime.date.today().__str__(),
                                     )

        cls.C = Event.objects.create(organizer=cls.organizer,
                                     name="TestEvent3C",
                                     status="C",
                                     start_date=datetime.date.today().__str__(),
                                     )

        cls.A1.categories.add(Category.objects.get(id=6))
        cls.A2.categories.add(Category.objects.get(id=6), Category.objects.get(id=7), Category.objects.get(id=8))
        cls.A3.categories.add(Category.objects.get(id=9))

    def test_user_sees_only_available_events_test(self):
        url = '/api/events/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], 3)

    def test_organizer_personal_area_sees_only_its_events(self):
        url = '/api/events/organizer/managed-events/'
        self.client.force_authenticate(user=self.organizer)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], 3)

    def test_filter_by_venue(self):
        url = '/api/events/?venue=TestVenue'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], 3)

    def test_filter_by_date_range(self):
        start_date = datetime.date.today().__str__()
        end_date = (datetime.date.today() + datetime.timedelta(days=1)).__str__()
        url = f'/api/events/?start_date={start_date}&end_date={end_date}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], 3)

    def test_filter_by_categories(self):
        url = '/api/events/?categories=9'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], 1)

    def test_user_interested_to_event(self):
        url = "/api/events/{}/interesting/".format(self.A1.id)
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, {"name": self.A1.name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user.username, json.loads(response.content)['interested'])

    def test_user_going_to_event(self):
        url = "/api/events/{}/going/".format(self.A1.id)
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, {"name": self.A1.name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user.username, json.loads(response.content)['participants'])

    def test_user_its_personal_interested_events(self):
        interesting_url = "/api/events/{}/interesting/".format(self.A1.id)
        personal_area_interested_url = '/api/events/user/personal-interested-events/'

        self.client.force_authenticate(user=self.user)
        self.client.post(interesting_url, {"name": self.A1.name})

        response = self.client.get(personal_area_interested_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], 1)

    def test_user_its_personal_going_events(self):
        going_url = "/api/events/{}/going/".format(self.A2.id)
        personal_area_going_url = '/api/events/user/personal-going-events/'

        self.client.force_authenticate(user=self.user)
        self.client.post(going_url, {"name": self.A2.name})

        response = self.client.get(personal_area_going_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["count"], 1)
