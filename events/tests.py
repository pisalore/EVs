import json
from events.models import Category
from users.models import EvUser
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class EventManagingTest(APITestCase):

    def setUp(self):
        Category.objects.bulk_create(
            [Category(category="Art & Culture"),
             Category(category="Food"),
             Category(category="Sport"),
             Category(category="Music"),
             Category(category="Other")]
        )
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
            "categories": [6]
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, test_event)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
