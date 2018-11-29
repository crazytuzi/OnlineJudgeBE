from django_filters import rest_framework
import django_filters
from .models import Submissions
from Utlis.NullFilter import NullFilter


class SubmissionsFilter(rest_framework.FilterSet):
    problem__problem_id = django_filters.NumberFilter()
    result = django_filters.NumberFilter()
    iscontest = NullFilter(field_name="contest")

    class Meta:
        model = Submissions
        fields = [
            'id',
            'user',
            'problem__problem_id',
            'result',
            'iscontest'
        ]
