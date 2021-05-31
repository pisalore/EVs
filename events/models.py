from django.db import models

from aws.models import AWSDocument
from users.models import EvUser
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    category = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.category


class Event(models.Model):
    class EventStatus(models.TextChoices):
        AVAILABLE = 'A', _('Available')
        SCHEDULED = 'S', _('Scheduled')
        CANCELED = 'C', _('Canceled')

    organizer = models.ForeignKey(EvUser, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=300, null=False)
    description = models.TextField(blank=True, null=True)
    profile_image = models.OneToOneField(AWSDocument, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=1, choices=EventStatus.choices, null=False)
    venue = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    start_hour = models.TimeField(blank=True, null=True)
    finish_hour = models.TimeField(blank=True, null=True)
    evs_link = models.URLField(blank=True, null=True)
    event_website = models.URLField(blank=True, null=True)
    tickets_website = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    interested = models.ManyToManyField(EvUser, blank=True, related_name='users_interested')
    participants = models.ManyToManyField(EvUser, blank=True, related_name='users_participants')

    def __str__(self):
        return self.name
