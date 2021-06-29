from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    modified_event_id = serializers.SerializerMethodField(read_only=True)
    user_has_read = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Notification
        exclude = ['event', 'notified']

    def get_modified_event_id(self, instance):
        return instance.event_id

    def get_user_has_read(self, instance):
        user = self.context['request'].user
        return instance.notification_item_notification.all().filter(user=user).first().user_has_read