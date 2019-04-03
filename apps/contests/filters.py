from django_filters import rest_framework
import django_filters
from .models import Contests
from django.utils import timezone


class ContestsFilter(rest_framework.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    state_filter = django_filters.NumberFilter(
        method='state_Filter', label='state')

    def state_Filter(self, queryset, name, value):
        if value == 0:
            return queryset.filter(start_time__gt=timezone.now())
        elif value == 2:
            return queryset.filter(end_time__lt=timezone.now())
        elif value == 1:
            return queryset.filter(
                start_time__lt=timezone.now(),
                end_time__gt=timezone.now())
        else:
            return queryset.none()

    class Meta:
        model = Contests
        fields = ['title', ]
