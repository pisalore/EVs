from rest_framework import serializers

from aws.api.serializers import AWSDocumentSerializer
from aws.models import AWSDocument
from events.models import Event, Category
from users.models import EvUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventSerializerAction(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField()
    interested = serializers.StringRelatedField(many=True, read_only=True)
    participants = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['name', 'organizer', 'interested', 'participants']


class EventSerializer(serializers.ModelSerializer):
    event_image = AWSDocumentSerializer(read_only=True)
    interested_count = serializers.SerializerMethodField(read_only=True)
    participants_count = serializers.SerializerMethodField(read_only=True)
    user_is_interested = serializers.SerializerMethodField(read_only=True)
    user_is_going = serializers.SerializerMethodField(read_only=True)
    organizer_username = serializers.SerializerMethodField(read_only=True)
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Event
        exclude = ['interested', 'participants']

    def get_interested_count(self, instance):
        return instance.interested.count()

    def get_participants_count(self, instance):
        return instance.participants.count()

    def get_user_is_interested(self, instance):
        request = self.context.get("request")
        return instance.interested.filter(pk=request.user.pk).exists()

    def get_user_is_going(self, instance):
        request = self.context.get("request")
        return instance.participants.filter(pk=request.user.pk).exists()

    def get_organizer_username(self, instance):
        return EvUser.objects.filter(pk=instance.organizer.id).first().username

    def validate(self, attrs):
        event_organizer = attrs.get('organizer')
        if not event_organizer.is_organizer:
            raise serializers.ValidationError('The event organizer MUST be an organizer.')
        return attrs


class EventImageSerializer(serializers.ModelSerializer):
    event_image = AWSDocumentSerializer(many=False)

    class Meta:
        model = Event
        fields = ["event_image"]

    def validate(self, attrs):
        if attrs.get('event_image').get('document'):
            document_ext = attrs.get('event_image').get('document').name.split('.')[-1].lower()
            if document_ext not in ['png', 'jpeg', 'jpg', ]:
                raise serializers.ValidationError('The file must be a JPEG or PNG image.')
        return attrs

    def update(self, instance, validated_data):
        event_image = validated_data.pop('event_image')
        document = event_image.get('document')
        aws_document = None
        if document:
            loaded_by = event_image.get('loaded_by')
            event = event_image.get('event')
            aws_document = AWSDocument.objects.create(document=document, event=event, loaded_by=loaded_by)

        instance.event_image = aws_document
        instance.save()

        return instance
