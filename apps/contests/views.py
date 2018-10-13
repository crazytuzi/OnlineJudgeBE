from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .models import Contests
from .serializers import ContestsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ContestsFilter

# Create your views here.


class ContestsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class ContestsListViewSet(
        CacheResponseMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """
    比赛列表页,分页,搜索,过滤,排序
    """
    queryset = Contests.objects.all()
    serializer_class = ContestsSerializer
    pagination_class = ContestsPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = ContestsFilter
    ordering_fields = ('start_time',)
