from django_filters import rest_framework
import django_filters
from .models import UserCollect


class UserCollectFilter(rest_framework.FilterSet):
    user__id = django_filters.NumberFilter()

    class Meta:
        model = UserCollect
        fields = ['user__id', ]
