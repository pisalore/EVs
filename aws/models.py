from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class AWSDocument(models.Model):
    class Meta:
        verbose_name_plural = 'AWS documents'

    class DocumentType(models.TextChoices):
        PROFILE_IMAGE = 'PI', _('Profile Image')
        EVENT_IMAGE = 'EI', _('Event Image')

    type = models.CharField(max_length=2, choices=DocumentType.choices)
    document = models.FileField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    loaded_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name='documents',
                                  null=True)

    def __str__(self):
        return '{}, {}'.format(type, self.document.name)
