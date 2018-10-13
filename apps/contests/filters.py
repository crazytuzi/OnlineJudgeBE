from django_filters import rest_framework
import django_filters
from .models import Contests


class ContestsFilter(rest_framework.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    contest_id = django_filters.NumberFilter()

    class Meta:
        model = Contests
        fields = ['title', 'problem_id']
