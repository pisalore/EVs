from django.db import models
from events.models import Event
from users.models import EvUser


class Notification(models.Model):
    type = models.CharField(max_length=20)
    message = models.CharField(max_length=128)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    members = models.ManyToManyField(EvUser, through='NotificationItem')

    def __str__(self):
        return self.type + " notification"


class NotificationItem(models.Model):
    user = models.ForeignKey(EvUser, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    user_has_read = models.BooleanField(default=False)
