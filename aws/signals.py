from aws.models import AWSDocument

from django.dispatch import receiver
from django.db.models.signals import post_delete


@receiver(post_delete, sender=AWSDocument)
def remove_file_from_s3(sender, instance, using, **kwargs):
    if instance:
        instance.document.delete(save=False)
