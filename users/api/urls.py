from django.urls import path
from users.api.views import CurrentUserAPIView, UserProfileAPIView, ProfileImageUpdateView

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path("user/profile/<str:username>/", UserProfileAPIView.as_view(), name="user-profile"),
    path("user/profile-image/", ProfileImageUpdateView.as_view(), name="profile-image"),
]
