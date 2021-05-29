from rest_framework import serializers
from aws.models import AWSDocument
from aws.api.serializers import AWSDocumentSerializer

from users.models import EvUser


class EvUserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EvUser
        fields = ["username", "organization_name", "is_organizer", "profile_image"]


class UserProfileImageSerializer(serializers.ModelSerializer):
    profile_image = AWSDocumentSerializer(many=False)

    class Meta:
        model = EvUser
        fields = ["profile_image"]

    def update(self, instance, validated_data):
        profile_image = validated_data.pop('profile_image')
        document = profile_image.get('document')
        aws_document = None
        if document:
            image_type = profile_image.get('type')
            loaded_by = profile_image.get('loaded_by')
            aws_document = AWSDocument.objects.create(document=document, type=image_type, loaded_by=loaded_by)

        instance.profile_image = aws_document
        instance.save()

        return instance
