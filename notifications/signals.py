from django.dispatch import receiver
from django.db.models.signals import post_save
from events.models import Event


@receiver(post_save, sender=Event)
def create_notification_for_participants_and_interested(sender, instance, using, **kwargs):
    print(instance.name)
