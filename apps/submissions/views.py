from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .models import Submissions
from .serializers import SubmissionsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SubmissionsFilter

# Create your views here.


class SubmissionsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 100


class SubmissionsListViewSet(
        CacheResponseMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionsSerializer
    pagination_class = SubmissionsPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = SubmissionsFilter
    ordering_fields = ('submit_time',)

    def perform_create(self,serializer):
        pass
