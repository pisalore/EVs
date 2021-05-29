from django.contrib.auth.models import AbstractUser, User
from django.db import models

from aws.models import AWSDocument


class EvUser(AbstractUser):
    organization_name = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    is_organizer = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    profile_image = models.OneToOneField(AWSDocument, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username
