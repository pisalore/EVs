from django.db import models


class AWSDocument(models.Model):
    type = models.CharField(max_length=140)
    document = models.FileField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'AWS documents'
