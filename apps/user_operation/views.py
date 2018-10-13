from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .models import UserCollect
from .serializers import UserCollectSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserCollectFilter

# Create your views here.


class UserCollectPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class UserCollectListViewSet(
        CacheResponseMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = UserCollect.objects.all()
    serializer_class = UserCollectSerializer
    pagination_class = UserCollectPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = UserCollectFilter
    ordering_fields = ('create_time',)
