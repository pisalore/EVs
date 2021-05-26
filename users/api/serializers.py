from rest_framework import serializers
from users.models import EvUser


class EvUserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EvUser
        fields = ["username", "organization_name", "is_organizer"]