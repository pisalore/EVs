from .views import UserNotificationsListAPIView, UserNotificationsReadView
from django.urls import path

urlpatterns = [
    path("notifications/", UserNotificationsListAPIView.as_view(), name="notifications"),
    path("notifications-read/", UserNotificationsReadView.as_view(), name="notifications-read"),
]
