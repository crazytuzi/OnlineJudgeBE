from django_filters import rest_framework
import django_filters
from .models import Submissions


class SubmissionsFilter(rest_framework.FilterSet):
    user__id = django_filters.NumberFilter()
    problem__problem_id = django_filters.NumberFilter()
    result = django_filters.NumberFilter()

    class Meta:
        model = Submissions
        fields = ['user__id', 'problem__problem_id', 'result']
