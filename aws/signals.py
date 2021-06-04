from aws.models import AWSDocument
from core.utils import generate_random_string
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete


@receiver(post_delete, sender=AWSDocument)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.document.delete(save=False)


@receiver(pre_save, sender=AWSDocument)
def add_id_to_s3_document_before_upload(sender, instance, *args, **kwargs):
    if instance.document.name:
        user_folder = instance.loaded_by.__str__() + '/'
        if instance.event:
            event_folder = '{}{}/'.format(settings.EVENT_PREFIX, instance.event.id)
            user_folder = user_folder + event_folder
        instance.document.name = user_folder + generate_random_string() + instance.document.name
