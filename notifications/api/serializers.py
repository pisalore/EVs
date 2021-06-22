from rest_framework import serializers

from notifications.models import Notification, NotificationItem


class NotificationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationItem
        exclude = ['user', 'notification']


class NotificationSerializer(serializers.ModelSerializer):
    modified_event_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Notification
        exclude = ['event', 'notified']

    def get_modified_event_id(self, instance):
        return instance.event_id