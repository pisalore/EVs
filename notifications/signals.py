from django.dispatch import receiver
from django.db.models.signals import pre_save
from events.models import Event
from .models import Notification, NotificationItem


@receiver(pre_save, sender=Event)
def create_notification_for_participants_and_interested(sender, instance, using, **kwargs):
    old_event = sender.objects.get(pk=instance.pk)
    if event_changed(instance):
        notification = Notification(event=instance)
        if instance.status == 'A' and old_event.status == 'A':
            notification.type = "changed"
            notification.message = f'The event {instance.name} has been changed. Please, check the event details page.'
        elif instance.status == 'A' and old_event.status == 'S':
            notification.type = "now available"
            notification.message = f'The event {instance.name} has scheduled and now is available! Please, check the ' \
                                   f'event details page. '
        elif instance.status == 'S' and old_event.status == 'A':
            notification.type = "TBA"
            notification.message = f'The organizer will reschedule the event {instance.name}. Stay tuned!'
        elif instance.status == 'C' and (old_event.status == 'A' or old_event.status == 'S'):
            notification.type = "canceled"
            notification.message = f'The organizer has canceled the event {instance.name}.'
        elif instance.status == 'A' and old_event.status == 'C':
            notification.type = "re-added"
            notification.message = f'The organizer has re-added the canceled event {instance.name}.'
        elif (instance.status == 'S' and old_event.status == 'S')\
                or (instance.status == 'C' and old_event.status == 'C'):
            return

        notification.save()
        notified_users = instance.participants.all() | instance.interested.all()
        for user in notified_users:
            user_notification = NotificationItem.objects.create(notification=notification, user=user)
            print(user_notification)


def event_changed(new_event):
    return not Event.objects.filter(
            name=new_event.name,
            description=new_event.description,
            status=new_event.status,
            venue=new_event.venue,
            start_date=new_event.start_date,
            finish_date=new_event.finish_date,
            start_hour=new_event.start_hour,
            finish_hour=new_event.finish_hour,
            event_website=new_event.event_website,
            tickets_website=new_event.tickets_website).exists()

