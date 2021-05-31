from django.urls import path

from events.api.views import EventsListAPIView, EventImageUpdateView

urlpatterns = [
    path("events/", EventsListAPIView.as_view(), name='all-events'),
    path("events/<int:pk>/image/", EventImageUpdateView.as_view(), name="event-image"),
]
