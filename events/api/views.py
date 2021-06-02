from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from events.api.serializers import CategorySerializer, EventSerializer, EventImageSerializer
from events.api.permissions import IsEventOrganizerOrReadOnly
from events.api.pagination import EventSetPagination
from events.models import Category, Event


class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('id')


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('start_date')
    serializer_class = EventSerializer
    permission_classes = [IsEventOrganizerOrReadOnly]
    pagination_class = EventSetPagination


class EventImageUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = EventImageSerializer
    permission_classes = [IsAuthenticated, IsEventOrganizerOrReadOnly]

    def get_object(self):
        event_id = self.kwargs.get('pk')
        event_object = Event.objects.filter(pk=event_id).first()
        return event_object

