from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

from django.shortcuts import get_object_or_404

from events.api.filters import EventFilter
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
    filterset_class = EventFilter
    filterset_fields = ['venue', 'categories']

    # Ordering by date using passed query params and search in date range
    def get_queryset(self):
        queryset = Event.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        ordering = self.request.query_params.get('ordering', 'start_date')
        if start_date and end_date:
            queryset = queryset.filter(start_date__range=[start_date, end_date])
        elif start_date:
            queryset = queryset.filter(start_date__gte=start_date)
        elif end_date:
            queryset = queryset.filter(start_date__lte=end_date)
        return queryset.filter(status='A').order_by(ordering)


class EventInterestAPIView(APIView):
    serializer_class = EventSerializerAction
    permission_classes = [IsAuthenticated]

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
        if event.participants.filter(id=user.id).exists():
            raise MethodNotAllowed(method='post', detail='You are participating to this event.')
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


class UserEventsPersonalAreaListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.user.username
        user_events_interested_in = Event.objects.filter(interested__username=username)
        user_events_going = Event.objects.filter(participants__username=username)
        queryset = user_events_interested_in | user_events_going
        return queryset.filter(status='A')


class OrganizerEventsPersonalAreaViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    pagination_class = EventSetPagination
    permission_classes = [IsAuthenticated, IsEventOrganizerOrReadOnly]

    def get_queryset(self):
        organizer = self.request.user
        return Event.objects.order_by('start_date').filter(organizer=organizer)
