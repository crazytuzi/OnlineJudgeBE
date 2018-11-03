from django_filters import rest_framework
import django_filters
from .models import Problems


class ProblemsFilter(rest_framework.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    problem_id = django_filters.NumberFilter()

    class Meta:
        model = Problems
        fields = ['title', 'problem_id']
