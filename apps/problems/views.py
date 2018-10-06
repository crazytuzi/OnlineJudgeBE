from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .models import Problems
from .serializers import ProblemsSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ProblemsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class ProblemsListViewSet(
        CacheResponseMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """
    题目列表页,分页,搜索,过滤,排序
    """
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    pagination_class = ProblemsPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ('_id',)
