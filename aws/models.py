from django.db import models
from django.conf import settings


class AWSDocument(models.Model):
    class Meta:
        verbose_name_plural = 'AWS documents'

    document = models.FileField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(settings.EVENT_MODEL,
                              on_delete=models.CASCADE,
                              related_name='event_images',
                              null=True)
    loaded_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name='user_images',
                                  null=True)

    def __str__(self):
        return self.document.name
