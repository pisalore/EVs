from django.dispatch import receiver
from django.db.models.signals import post_delete
from users.models import EvUser

from evsapp import settings
from core.utils import delete_related_user_files_s3


@receiver(post_delete, sender=EvUser)
def remove_file_from_s3(sender, instance, using, **kwargs):
    if settings.USE_S3:
        delete_related_user_files_s3(instance.username)


