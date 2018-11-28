from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import UserCollect, UserAcceptedProblems
from .serializers import UserCollectSerializer, UserAcceptedProblemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserCollectFilter, UserAcceptedProblemFilter

# Create your views here.


class UserCollectPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class UserCollectListViewSet(
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


class UserAcceptedProblemListViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = UserAcceptedProblems.objects.all()
    serializer_class = UserAcceptedProblemSerializer
    pagination_class = UserCollectPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = UserAcceptedProblemFilter
    ordering_fields = ('create_time',)
