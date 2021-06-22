from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from .serializers import NotificationSerializer
from notifications.models import Notification


class UserNotificationsListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.order_by('created_at').filter(notified__username=user.username)
