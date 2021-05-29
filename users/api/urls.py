from django.urls import path
from users.api.views import CurrentUserAPIView, ProfileImageUpdateView

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path("user/profile-image/", ProfileImageUpdateView.as_view(), name="profile-image"),
]
