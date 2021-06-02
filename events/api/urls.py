from django.urls import include, path
from rest_framework.routers import DefaultRouter
from events.api.views import CategoryListAPI, EventViewSet, EventImageUpdateView

router = DefaultRouter()
router.register(r"events", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("categories/", CategoryListAPI.as_view(), name="categories"),
    path("events/<int:pk>/image/", EventImageUpdateView.as_view(), name="event-image"),
]
