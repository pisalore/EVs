from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from events.api.serializers import CategorySerializer, EventSerializer, EventImageSerializer, EventSerializerAction
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


class EventInterestAPIView(APIView):
    serializer_class = EventSerializerAction
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'delete']

    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        user = self.request.user

        event.interested.remove(user)
        event.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(event, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        user = self.request.user

        event.interested.add(user)
        event.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(event, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EventGoingAPIView(APIView):
    serializer_class = EventSerializerAction
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'delete']

    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        user = self.request.user

        event.participants.remove(user)
        event.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(event, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        user = self.request.user
        if event.interested.filter(id=user.id).exists():
            event.interested.remove(user)
        event.participants.add(user)
        event.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(event, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EventImageUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = EventImageSerializer
    permission_classes = [IsAuthenticated, IsEventOrganizerOrReadOnly]

    def get_object(self):
        event_id = self.kwargs.get('pk')
        event_object = Event.objects.filter(pk=event_id).first()
        return event_object
