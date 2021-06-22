from .views import UserNotificationsListAPIView
from django.urls import path

urlpatterns = [
    path("notifications/", UserNotificationsListAPIView.as_view(), name="notifications"),
]
