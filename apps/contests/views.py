from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Contests, ContestRankList
from .serializers import ContestsSerializer, ContestRankListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ContestsFilter, ContestRankListFilter

# Create your views here.


class ContestsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class ContestsListViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
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


class ContestRankListViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = ContestRankList.objects.all()
    serializer_class = ContestRankListSerializer
    pagination_class = ContestsPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = ContestRankListFilter
    ordering_fields = ('-accepted', 'preaccepted_time', 'create_time')
