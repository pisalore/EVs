from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from events.api.serializers import EventSerializer, EventImageSerializer
from events.api.permissions import IsEventOrganizerOrReadOnly
from events.models import Event


class EventsListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventImageUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = EventImageSerializer
    permission_classes = [IsAuthenticated, IsEventOrganizerOrReadOnly]

    def get_object(self):
        event_id = self.kwargs.get('pk')
        event_object = Event.objects.filter(pk=event_id).first()
        return event_object

