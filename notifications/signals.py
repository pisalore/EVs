from django.dispatch import receiver
from django.db.models.signals import post_save
from events.models import Event
from .models import Notification, NotificationItem


@receiver(post_save, sender=Event)
def create_notification_for_participants_and_interested(sender, instance, using, **kwargs):
    notification = Notification()
    if instance.status == 'A':
        notification.type = "changed"
        notification.message = f'The event {instance.name} has been changed. Please, check the event details page.'
    elif instance.status == 'S':
        notification.type = "TBA"
        notification.message = f'The organizer will reschedule the event {instance.name}. Stay tuned!'
    elif instance.status == 'C':
        notification.type = "canceled"
        notification.message = f'The organizer has canceled the event {instance.name}.'
    notification.event = instance
    notification.save()
