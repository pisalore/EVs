from django_filters import rest_framework as filters
from events.models import Event


class EventFilter(filters.FilterSet):
    events = filters.CharFilter(
        field_name='categories__category',
        lookup_expr='exact',
    )

    venue = filters.CharFilter(
        field_name='venue',
        lookup_expr='contains',
    )

    class Meta:
        model = Event
        fields = ['categories', 'venue']