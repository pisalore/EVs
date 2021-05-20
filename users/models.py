from django.contrib.auth.models import AbstractUser, User
from django.db import models


class EvUser(AbstractUser):
    organization_name = models.CharField(max_length=240)
    city = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    is_organizer = models.BooleanField(default=False)
