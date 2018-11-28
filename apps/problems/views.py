from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Problems
from .serializers import ProblemsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProblemsFilter

# Create your views here.


class ProblemsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class ProblemsListViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    pagination_class = ProblemsPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = ProblemsFilter
    ordering_fields = ('problem_id',)
