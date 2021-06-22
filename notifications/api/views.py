from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import NotificationSerializer
from notifications.models import Notification, NotificationItem


class UserNotificationsListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.order_by('-created_at').filter(notified__username=user.username)


class UserNotificationsReadView(APIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_notification_items = NotificationItem.objects \
            .filter(user=request.user) \
            .filter(user_has_read=False)
        for notification in user_notification_items:
            notification.user_has_read = True
            notification.save()
        return Response({"message": "notifications set as read."}, status=status.HTTP_200_OK)
