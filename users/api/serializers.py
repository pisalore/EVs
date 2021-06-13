from rest_framework import serializers
from aws.models import AWSDocument
from aws.api.serializers import AWSDocumentSerializer

from users.models import EvUser


class EvUserDisplaySerializer(serializers.ModelSerializer):
    profile_image = AWSDocumentSerializer(read_only=True)

    class Meta:
        model = EvUser
        fields = ["id", "username", "first_name", "last_name", "email", "organization_name", "is_organizer", "profile_image"]


class UserProfileSerializer(serializers.ModelSerializer):
    profile_image = AWSDocumentSerializer(read_only=True)
    is_organizer = serializers.BooleanField(read_only=True)

    class Meta:
        model = EvUser
        fields = ['first_name', 'last_name', 'organization_name', 'city', 'birthday', 'is_organizer', 'username',
                  'email', 'profile_image']


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
            loaded_by = profile_image.get('loaded_by')
            aws_document = AWSDocument.objects.create(document=document, loaded_by=loaded_by)

        instance.profile_image = aws_document
        instance.save()

        return instance


class RequestFormSerializer(serializers.Serializer):
    user_email = serializers.EmailField(allow_blank=False)
    username = serializers.CharField(max_length=150)
    user_message = serializers.CharField(max_length=300)
