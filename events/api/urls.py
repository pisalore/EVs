from django.urls import include, path
from rest_framework.routers import DefaultRouter
from events.api.views import CategoryListAPI, EventImageUpdateView, EventViewSet, EventGoingAPIView, \
    EventInterestAPIView, OrganizerEventsPersonalAreaViewSet, UserEventsPersonalAreaListView

router = DefaultRouter()
router.register(r"events", EventViewSet)
router.register(r"events/organizer/managed-events", OrganizerEventsPersonalAreaViewSet, basename='managed-events')

urlpatterns = [
    path("", include(router.urls)),
    path("categories/", CategoryListAPI.as_view(), name="categories"),
    path("events/<int:pk>/image/", EventImageUpdateView.as_view(), name="event-image"),
    path("events/<int:pk>/interesting/", EventInterestAPIView.as_view(), name="event-interest"),
    path("events/<int:pk>/going/", EventGoingAPIView.as_view(), name="event-interest"),
    path("events/user/personal-events/", UserEventsPersonalAreaListView.as_view(), name='personal-events'),
]