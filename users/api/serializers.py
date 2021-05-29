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

    def validate(self, attrs):
        if attrs.get('profile_image').get('document'):
            document_ext = attrs.get('profile_image').get('document').name.split('.')[-1].lower()
            if document_ext not in ['png', 'jpeg', 'jpg', ]:
                raise serializers.ValidationError('The file must be a JPEG or PNG image.')
        return attrs

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
